"""Platzigram views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def time(request):
    """ "The server time"""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse("{now}".format(now=now))


def order_numbers(request):
    """Retorn sorted integers"""
    numbers = sorted([int(number) for number in request.GET["numbers"].split(",")])
    data = {
        "status": "ok",
        "numbers": numbers,
        "message": "Numbers sorted succesfully.",
    }

    return HttpResponse(json.dumps(data), content_type="application/json")
