# Create your views here.
import nltk
from django.db.models import Count, Avg
from django.http import HttpResponse
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from analyzer.models import TweetSummary, FinalTable, FinalTableAll
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
    return HttpResponse("Country info will be added to summary using opencagedata..")


def generate_final_table(request):
    delete_everything_from_final_table()
    entities = get_top_100_entities()
    for entity in entities:
        for date in set(TweetSummary.objects.filter(entity=entity[0]).values_list('date')):
            final_row = FinalTableAll(
                entity=entity[0],
                date=date,
                semantic_compound=
                TweetSummary.objects.all().filter(entity=entity[0]).aggregate(Avg('semantic_compound'))[
                    'semantic_compound__avg']
            )
            final_row.save()
    return HttpResponse("Country info will be added to summary using opencagedata..")


def delete_everything_from_final_table():
    FinalTable.objects.all().delete()


def get_top_100_entities():
    entity_list = TweetSummary.objects.values_list('entity').annotate(entity_count=Count('entity')) \
        .order_by('-entity_count')
    return entity_list[:100]
