from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from get_movie.web_scrape import get_top_movies

def get_movies(request):
    genre = request.GET.get("genre", "")
    movies = get_top_movies(genre)
    # return HttpResponse("Hiiiiiiii")
    return JsonResponse(movies, safe=False)