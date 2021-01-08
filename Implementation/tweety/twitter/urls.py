from django.urls import path

from twitter import views

urlpatterns = [
    path('start/', views.start_twitter_calls, name='start_twitter_call'),
    path('stop/', views.stop_twitter_calls, name='stop_twitter_call'),
]