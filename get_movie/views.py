from django.shortcuts import render
from django.http import HttpResponse

def get_movies(request):
    return HttpResponse("Hello World")