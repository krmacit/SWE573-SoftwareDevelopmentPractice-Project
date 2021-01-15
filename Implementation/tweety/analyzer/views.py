# Create your views here.
import nltk
from django.http import HttpResponse
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from twitter.models import Tweet


def analyzer(request):
    tweets = Tweet.objects.all()[:10]
    print(tweets)

    texts = set(tweet.text for tweet in tweets)

    sentiment_analyzer(texts)

    return HttpResponse("Called")


def sentiment_analyzer(text):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    for t in text:
        print(t)
        print(sid.polarity_scores(t))
