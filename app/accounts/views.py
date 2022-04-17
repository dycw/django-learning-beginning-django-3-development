from typing import Any

from accounts.forms import UserCreateForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


def signupaccount(request: HttpRequest) -> HttpResponse:
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
    return render(request, "signupaccount.html", context)
