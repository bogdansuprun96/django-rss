from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.


def index(request):
    number = random.randrange(0, 100)
    # return HttpResponse("Hi")
    context = {
        'value': 'Hello Python',
        'title': 'Hello Django!',
        'number': str(number),
    }
    return render(request, "index.html", context)
