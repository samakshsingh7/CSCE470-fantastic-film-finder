from django.db import models
from django.forms import CharField

# Create your models here.
class Movie(models.Model):
    imdbID = CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits= 3, decimal_places= 1)
    genres = models.CharField(max_length= 200)
    isAdult = models.BooleanField()
    runTimeMinutes = models.IntegerField()
    releaseYear = models.CharField(max_length= 50)
    numVotes = models.IntegerField()
    # directors = models.CharField()