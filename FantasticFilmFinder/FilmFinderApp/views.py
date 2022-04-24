from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .DF import printer
from .models import Movie, Genre
import pandas as pd
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def printerofnum(request):
    # insert dataframe code here
    # item = Movie.objects.all().values()
    # df = pd.DataFrame(item)
    # mydict = {
    #     "df": df.to_html()
    # }
    # return render(request, 'DF.html', context=mydict)
    
    result = printer()
    return HttpResponse(result)
    # return render(request, 'DF.html', {'result':result})

def movie_by_id(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return HttpResponse(f"Movie: {movie.title}, genre is {movie.genres}")

def genres(request):
    # if request.method == 'POST':
    #     context = {'request.POST':request.POST}
    #     return redirect(request, 'list.html', context)
    #TODO
    #allgenres = all unique genres in csv
    allGenres = Genre.objects.all()
    return render(request, 'genres.html', {'allGenres': allGenres})

def home(request):
    return render(request, 'home.html')

def listGenre(request):
    if request.method == 'POST':
        genre_id = request.POST['button']
        print(genre_id)
    #TODO
    #use genre_id to call script and return movies in that genre
    item = Movie.objects.all().filter(genres=genre_id).values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return HttpResponse(df.to_html())
    return render(request, 'DF.html', context=mydict)