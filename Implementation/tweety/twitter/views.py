from django.http import HttpResponse

from twitter import services
from twitter.models import TwitterUser


def start_twitter_calls(request):
    services.make_twitter_call()
    return HttpResponse(TwitterUser.objects.all())


def stop_twitter_calls(request):
    return HttpResponse("Calls stopped..")
