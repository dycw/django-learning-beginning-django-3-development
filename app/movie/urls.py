from django.urls import path
from movie.views import create_review
from movie.views import delete_review
from movie.views import detail
from movie.views import update_review


urlpatterns = [
    path("<int:movie_pk>/", detail, name="detail"),
    path("<int:movie_pk>/create/", create_review, name="create_review"),
    path("review/<int:review_pk>/", update_review, name="update_review"),
    path("review/<int:review_pk>/delete", delete_review, name="delete_review"),
]
