from django.http import HttpResponse

from twitter import services
from twitter.models import TwitterUser, Tweet, Entities


def start_twitter_calls(request):
    services.make_twitter_call()
    return HttpResponse(TwitterUser.objects.all())


def stop_twitter_calls(request):
    return HttpResponse("Calls will be stopped..")


def remove_any_duplicates_in_tweets(request):
    for row in Tweet.objects.all().reverse():
        if Tweet.objects.filter(id=row.id).count() > 1:
            row.delete()
    for row in Entities.objects.all().reverse():
        if Entities.objects.filter(tweet_id_id=row.tweet_id_id).filter(normalized_text=row.normalized_text).count() > 1:
            row.delete()
    return HttpResponse("Calls will be stopped..")
