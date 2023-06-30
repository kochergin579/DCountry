
from django.contrib import admin
from django.urls import path
from MainApp import views






urlpatterns = [
        path('', views.home, name='home'),
        path('countries/', views.countries_list, name="countries_list"),
        path('country/<id>/', views.country_page, name="country_page"),
        path('languages/', views.languages_list, name="languages_list"),


]
