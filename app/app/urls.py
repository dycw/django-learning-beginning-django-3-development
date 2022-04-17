from django.contrib.admin import site
from django.urls import path
from movie.views import about
from movie.views import home

urlpatterns = [
    path("admin/", site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
]
