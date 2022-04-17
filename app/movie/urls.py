from django.urls import path
from movie.views import create_review
from movie.views import detail


urlpatterns = [
    path("<int:movie_pk>/", detail, name="detail"),
    path("<int:movie_pk>/create/", create_review, name="create_review"),
]
