from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.urls import include
from django.urls import path
from movie.views import about
from movie.views import home
from movie.views import signup

urlpatterns = [
    path("admin/", site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("signup/", signup, name="signup"),
    path("news/", include("news.urls")),
]
urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
