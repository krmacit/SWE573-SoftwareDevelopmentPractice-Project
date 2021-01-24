# Create your views here.
import nltk
from django.db.models import Count, Avg
from django.http import HttpResponse
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from opencage.geocoder import OpenCageGeocode, RateLimitExceededError

from analyzer.models import TweetSummary, FinalTableAll, FinalTable
from twitter.models import Tweet, Entities


def analyzer(request):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    tweets = Tweet.objects.all()
    for tweet in tweets:
        if not TweetSummary.objects.filter(tweet_id=tweet.id).exists():
            for entity in Entities.objects.filter(tweet_id=tweet.id):
                scores = sid.polarity_scores(tweet.text)
                user = tweet.author_id
                tweet_analysis = TweetSummary(
                    tweet_id=tweet.id,
                    entity=entity.normalized_text,
                    date=tweet.date,
                    semantic_neg=scores["neg"],
                    semantic_neu=scores["neu"],
                    semantic_pos=scores["pos"],
                    semantic_compound=scores["compound"],
                    location=user.location,
                    country_code=None
                )
                tweet_analysis.save()
    return HttpResponse("All Tweets are copied to tweetsummarytable")


def add_country(request):
    key = '9ef7cd1fb7154263b30d1222657ae2d4'
    geocoder = OpenCageGeocode(key)
    try:
        for tweetSummary in TweetSummary.objects.all():
            if tweetSummary.country is None and tweetSummary.location is not None:
                results = geocoder.geocode(tweetSummary.location)
                if len(results) > 0 and 'components' in results[0] and 'country' in results[0]['components']:
                    tweetSummary.country = results[0]['components']['country']
                    tweetSummary.country_code = results[0]['components']['country_code']
                    tweetSummary.continent = results[0]['components']['continent']
                else:
                    tweetSummary.location = None
                tweetSummary.save()
    except RateLimitExceededError as ex:
        print(ex)
    return HttpResponse("Country info will be added to summary using open cage data..")


def generate_final_table(request):
    delete_everything_from_final_table()
    entities = get_top_entities()
    for entity in entities:
        for current_date in set(TweetSummary.objects.filter(entity=entity[0]).values_list('date')):
            final_row = FinalTableAll(
                entity=entity[0],
                date=current_date[0],
                semantic_compound=TweetSummary.objects.all().filter(entity=entity[0]).filter(
                    date=current_date[0]).aggregate(Avg('semantic_compound'))['semantic_compound__avg'],
                tweet_count=TweetSummary.objects.all().filter(entity=entity[0]).filter(
                    date=current_date[0]).aggregate(Count("entity"))['entity__count']
            )
            final_row.save()
    return HttpResponse("Final Table are regenerated..")


def delete_everything_from_final_table():
    FinalTableAll.objects.all().delete()


def get_top_entities():
    entity_list = TweetSummary.objects.values_list('entity').annotate(entity_count=Count('entity')) \
        .order_by('-entity_count')
    return entity_list[:25]


def generate_region_final_table(request):
    delete_everything_from_region_final_table()
    entities = get_top_entities()
    for entity in entities:
        for current_date in set(TweetSummary.objects.filter(entity=entity[0]).values_list('date')):
            for current_region in get_regions():
                final_row = FinalTable(
                    entity=entity[0],
                    date=current_date[0],
                    region=current_region,
                    semantic_compound=TweetSummary.objects.all().filter(entity=entity[0]).filter(
                        date=current_date[0]).filter(continent=current_region).aggregate(Avg('semantic_compound'))['semantic_compound__avg'],
                    tweet_count=TweetSummary.objects.all().filter(entity=entity[0]).filter(
                        date=current_date[0]).filter(continent=current_region).aggregate(Count("entity"))['entity__count']
                )
                final_row.save()
    return HttpResponse("Final Table are regenerated..")


def get_regions():
    return ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]


def delete_everything_from_region_final_table():
    FinalTable.objects.all().delete()