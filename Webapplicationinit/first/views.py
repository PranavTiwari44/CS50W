from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")# Create your views here.

def user(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
