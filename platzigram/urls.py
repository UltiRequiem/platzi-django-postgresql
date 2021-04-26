"""Platzigram URLS"""


from django.urls import path
from django.http import HttpResponse

def hello(request):
    """"Return Hello World"""
    return HttpResponse("Hello World")




urlpatterns = [path('hello/',hello)]
