from typing import Any

from accounts.forms import UserCreateForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


def signup_account(request: HttpRequest, /) -> HttpResponse:
    context: dict[str, Any] = {"form": UserCreateForm}
    if request.method == "POST":
        post = request.POST
        if (password := post["password1"]) == post["password2"]:
            try:
                user = User.objects.create_user(  # type: ignore
                    post["username"], password=password
                )
            except IntegrityError:
                context[
                    "error"
                ] = "Username already taken. Choose new username."
            else:
                user.save()
                login(request, user)
                return redirect("home")
        else:
            context["error"] = "Passwords do not match"
    return render(request, "signup_account.html", context)


@login_required
def logout_account(request: HttpRequest, /) -> HttpResponse:
    logout(request)
    return redirect("home")


def login_account(request: HttpRequest, /) -> HttpResponse:
    context: dict[str, Any] = {"form": AuthenticationForm}
    if request.method == "POST":
        post = request.POST
        if (
            user := authenticate(
                request, username=post["username"], password=post["password"]
            )
        ) is None:
            context["error"] = "User name and password do not match"
        else:
            login(request, user)
            return redirect("home")
    return render(request, "login_account.html", context)
