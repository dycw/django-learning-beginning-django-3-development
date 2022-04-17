from django.contrib.admin import site
from movie.models import Movie
from movie.models import Review


site.register(Movie)
site.register(Review)
