from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list, name='countries_list'),
    path('countries-list/<str:country_name>/', views.countries_list_detail, name='detail'),
    path('languages-list', views.languages_list, name='languages_list'),
]
