from accounts.views import signupaccount
from django.urls import path


urlpatterns = [path("signupaccount/", signupaccount, name="signupaccount")]
