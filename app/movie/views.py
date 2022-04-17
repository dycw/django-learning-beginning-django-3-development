from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html", {"name": "Greg Lim"})


def about(_: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to About Page</h1>")
