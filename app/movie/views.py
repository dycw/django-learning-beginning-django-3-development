from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from movie.models import Movie


def home(request: HttpRequest) -> HttpResponse:
    if search_term := request.GET.get("search_movie"):
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    return render(
        request, "home.html", {"search_term": search_term, "movies": movies}
    )


def about(_: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to About Page</h1>")


def signup(request: HttpRequest) -> HttpResponse:
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})
