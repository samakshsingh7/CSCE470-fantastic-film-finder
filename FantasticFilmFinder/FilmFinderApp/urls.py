from django.urls import path

from . import views
from .views import printerofnum

urlpatterns = [
    path('', views.index, name='index'),
    path('print', views.printerofnum, name='print'),
    path('movie/<int:movie_id>', views.movie_by_id, name='book_by_id'),
]