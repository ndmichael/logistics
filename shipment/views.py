from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

# Create your views here.


def index (request):
    return HttpResponse("<h1>testing about us </h1>")

def about (request):
    pass

def contact (request):
    pass