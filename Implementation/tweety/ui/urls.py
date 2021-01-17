from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('country/', views.country_page, name='country'),
    path('info/', views.info_page, name='info'),
    path('contact/', views.contact_page, name='contact'),
    path('register/', views.register, name='register'),
]