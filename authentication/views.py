from django.shortcuts import render, redirect
from django.contrib.auth import login


def index(request):
    return render(request, "authentication/index.html", {})


def signup(request):
    return render(request, "authentication/signup.html", {})


def login(request):
    return render(request, "authentication/login.html", {})
