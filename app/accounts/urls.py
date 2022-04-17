from accounts.views import loginaccount
from accounts.views import logoutaccount
from accounts.views import signupaccount
from django.urls import path


urlpatterns = [
    path("signupaccount/", signupaccount, name="signupaccount"),
    path("logout/", logoutaccount, name="logoutaccount"),
    path("login/", loginaccount, name="loginaccount"),
]
