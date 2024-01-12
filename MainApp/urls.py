from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/<int:num_page>/', views.countries_list, name='countries_list'),
    path('countries-list/<str:country_name>/', views.countries_list_detail, name='country_detail'),
    path('sorting/<str:letter>/', views.sorting, name='sorting'),
    path('languages-list', views.languages_list, name='languages_list'),
    path('languages-list/<str:language_name>', views.languages_list_detail, name='language_detail'),
]
