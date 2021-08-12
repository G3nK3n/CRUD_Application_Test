from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Motoneiges


# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello  World</h1>")
    return render(request, "home.html", {})

def add_view(request, *args, **kwargs):
    my_context = {
        "my_text":"This is a test text",
        "my_number":123,
        "my_list":[123, 456, 789]
    }
    return render(request, "add.html", my_context)


