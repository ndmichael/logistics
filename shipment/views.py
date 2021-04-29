from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

# Create your views here.


def index (request):
    return render(request, 'shipment/index.html')

def about (request):
    return render(request, 'shipment/about.html')

def track (request):
        return render(request, 'shipment/track.html')

def services (request):
    return render(request, 'shipment/services.html')

def contact (request):
    return render(request, 'shipment/contact.html')