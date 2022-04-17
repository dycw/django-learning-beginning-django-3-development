from accounts.views import login_account
from accounts.views import logout_account
from accounts.views import signup_account
from django.urls import path


urlpatterns = [
    path("signup/", signup_account, name="signup_account"),
    path("logout/", logout_account, name="logout_account"),
    path("login/", login_account, name="login_account"),
]
