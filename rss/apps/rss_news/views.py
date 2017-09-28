from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.


def index(request):
    number = random.randrange(0, 100)
    # return HttpResponse("Hi")
    context = {
        'title': 'Portfolio',
        'name': 'Bohdan',
        'surname': 'Suprun',
        'speciality': 'Python, Django Programmer',
    }
    return render(request, "index.html", context)
