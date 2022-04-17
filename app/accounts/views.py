from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def signupaccount(request: HttpRequest) -> HttpResponse:
    return render(request, "signupaccount.html", {"form": UserCreationForm})
