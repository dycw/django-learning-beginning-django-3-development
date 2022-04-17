from django.urls import path
from movie.views import detail


urlpatterns = [path("<int:movie_id>", detail, name="detail")]
