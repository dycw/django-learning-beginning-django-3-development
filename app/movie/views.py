from typing import Any

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from movie.forms import ReviewForm
from movie.models import Movie
from movie.models import Review


def home(request: HttpRequest, /) -> HttpResponse:
    if search_term := request.GET.get("search_movie"):
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    return render(
        request, "home.html", {"search_term": search_term, "movies": movies}
    )


def about(_: HttpRequest, /) -> HttpResponse:
    return HttpResponse("<h1>Welcome to About Page</h1>")


def signup(request: HttpRequest, /) -> HttpResponse:
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def detail(request: HttpRequest, /, *, movie_pk: int) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.filter(movie=movie)
    return render(request, "detail.html", {"movie": movie, "reviews": reviews})


def create_review(request: HttpRequest, /, *, movie_pk: int) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=movie_pk)
    context: dict[str, Any] = {"form": ReviewForm, "movie": movie}
    if request.method == "POST":
        form = ReviewForm(request.POST)
        try:
            review = form.save(commit=False)
        except ValueError:
            context["error"] = "bad data passed in"
        else:
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect("detail", review.movie.pk)
    return render(request, "create_review.html", context)
