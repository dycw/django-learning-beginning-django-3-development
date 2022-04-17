from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    search_term = request.GET.get("search_movie")
    return render(request, "home.html", {"search_term": search_term})


def about(_: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to About Page</h1>")


def signup(request: HttpRequest) -> HttpResponse:
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})
