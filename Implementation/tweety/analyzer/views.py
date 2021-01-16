# Create your views here.
import geocoder
import nltk
from django.http import HttpResponse
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from analyzer.models import TweetSummary
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
                g = geocoder.google(user.location)
                print(g)
                tweet_analysis = TweetSummary(
                    tweet_id=tweet.id,
                    entity=entity.normalized_text,
                    date=tweet.date,
                    semantic_neg=scores["neg"],
                    semantic_neu=scores["neu"],
                    semantic_pos=scores["pos"],
                    semantic_compound=scores["neg"],
                    location=user.location,
                    country=None
                )
                tweet_analysis.save()
    return HttpResponse("All Tweets are copied to summary")


def add_country(request):
    return HttpResponse("Country info will be added to summary using opencagedata..")
