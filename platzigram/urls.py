"""Platzigram URLS"""

from platzigram import views

from django.urls import path

urlpatterns = [
        path("time/", views.time),
        path("order-numbers/", views.order_numbers)
        ]
