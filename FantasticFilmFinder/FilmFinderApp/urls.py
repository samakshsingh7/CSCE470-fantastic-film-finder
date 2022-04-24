from django.urls import path

from . import views
from .views import printerofnum

urlpatterns = [
    path('index', views.index, name='index'),
    path('print', views.printerofnum, name='print'),
    path('movie/<int:movie_id>', views.movie_by_id, name='book_by_id'),
    path('genres/', views.genres, name='genres'),
    path('', views.home, name='home'),
    path('list', views.listGenre, name='list'),
]