from django.shortcuts import render

from django.http import *

def index(request):
    return HttpResponse("Hello, world. YOu're at the polls index")
# Create your views here.
