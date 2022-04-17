from django.db.models import CharField
from django.db.models import ImageField
from django.db.models import Model
from django.db.models import URLField


class Movie(Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="movie/images/")
    url = URLField(blank=True)
