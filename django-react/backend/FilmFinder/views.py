from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FilmSerializer
from .models import Film

# Create your views here.

class FilmView(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
# Create your views here.
class GenreView(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()