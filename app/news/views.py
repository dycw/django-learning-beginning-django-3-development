from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from news.models import News


def news(request: HttpRequest, /) -> HttpResponse:
    newss = News.objects.all()
    return render(request, "news.html", {"newss": newss})
