from django.urls import path
from .views import scrape,clear

urlpatterns = [
    path('',scrape,name='scrape'),
    path('delete/',clear,name='clear')   
]
