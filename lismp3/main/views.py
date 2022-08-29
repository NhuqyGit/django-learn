from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1> hello world</h1>")

def hello(response):
    return HttpResponse("<h1>CCCCCCCCCC</h1>")