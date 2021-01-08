from django.http import HttpResponse


def start_twitter_calls(request):
    return HttpResponse("Twitter calls started..")


def stop_twitter_calls(request):
    return HttpResponse("Calls stopped..")
