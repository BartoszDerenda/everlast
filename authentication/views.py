from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "authentication/index.html", {})


def signup(request):
    return render(request, "authentication/signup.html", {})


def login(request):
    return render(request, "authentication/login.html", {})
