from django.urls import path

from analyzer import views

urlpatterns = [
    path('start/', views.analyzer, name='analyzer')
]