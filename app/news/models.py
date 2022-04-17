from django.db.models import CharField
from django.db.models import DateField
from django.db.models import Model
from django.db.models import TextField


class News(Model):
    headline = CharField(max_length=200)
    body = TextField()
    date = DateField()

    def __str__(self) -> str:
        return self.headline
