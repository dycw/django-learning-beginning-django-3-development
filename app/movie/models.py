from django.contrib.auth.models import User
from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import ImageField
from django.db.models import Model
from django.db.models import URLField


class Movie(Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="movie/images/")
    url = URLField(blank=True)


class Review(Model):
    text = CharField(max_length=100)
    date = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, on_delete=CASCADE)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    watch_again = BooleanField()

    def __str__(self) -> str:
        return self.text
