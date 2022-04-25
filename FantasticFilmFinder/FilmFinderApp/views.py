from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .DF import *
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
    genreArray = sorted(listGenresDF())
    allGenres = Genre.objects.all()
    return render(request, 'genres.html', {'genreArray': genreArray})

def home(request):
    return render(request, 'home.html')

def listGenre(request):
    if request.method == 'POST':
        genre_id = request.POST['button']
        print(genre_id)
    #TODO
    #use genre_id to call script and return movies in that genre
    #MODIFY FUNCTION HERE FOR GENRE
    df = pd.DataFrame(genreListDF(genre_id))
    # df = genreListDF(genre_id)
    # df = pd.DataFrame.from_records(genreListDF(genre_id))
    # item = Movie.objects.all().filter(genres=genre_id).values()
    # df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return HttpResponse(df.to_html())
    return render(request, 'DF.html', context=mydict)
def search(request):
    return render(request, 'search.html')

def displaySearch(request):
    #gets single word genre
    if request.method == 'POST':
        contains = request.POST['name']
        # print(contains)
    #TODO
    #use contains to call script and return movies that contain that string in title
    # item = Movie.objects.all().filter(title=contains).values()
    # df = pd.DataFrame(item)
    #MODIFY FUNCTION HERE FOR SEARCH/VSM
    df = pd.DataFrame(get_top_score_for_query(contains))
    mydict = {
        "df": df.to_html()
    }
    return HttpResponse(df.to_html())