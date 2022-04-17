from django.contrib.admin import site
from movie.models import Movie


site.register(Movie)
