from django.contrib import admin
from django.urls import path, include
from . import views
from .views import vivod_glav_str, submit_volunteer_application, news_page

urlpatterns = [
    path('', vivod_glav_str),
    path('submit-volunteer/', views.submit_volunteer_application, name='submit_volunteer'),
    path('animals/', views.animals_page, name='animals'),
    path('news/', views.news_page),
    path('reports/', views.reports_page, name='reports')
]
