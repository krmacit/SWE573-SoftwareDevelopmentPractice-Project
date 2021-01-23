from django.urls import path

from analyzer import views

urlpatterns = [
    path('addtosummary/', views.analyzer, name='analyzer'),
    path('addcountry/', views.add_country, name='add_country'),
    path('generatefinal/', views.generate_final_table, name='final_table'),
    path('generateregionfinal/', views.generate_region_final_table, name='final_table_region')
]
