from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .DF import printer
from .models import Movie
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def printerofnum(request):
    
    result = printer()
    return render(request, 'DF.html', {'result':result})

def movie_by_id(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return HttpResponse(f"Movie: {movie.title}, genre is {movie.genres}")