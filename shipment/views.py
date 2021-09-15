from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from shipment.forms import ItemTrackForm
from shipment.models import ItemDetail

# Create your views here.


def index (request):
    return render(request, 'shipment/index.html')

def about (request):
    return render(request, 'shipment/about.html')

def track_item (request):
    form = ItemTrackForm
    if 'q' in request.GET:
        form = ItemTrackForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            item = ItemDetail.objects.get(item_code=q)
            
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'shipment/track.html', context)

def services (request):
    return render(request, 'shipment/services.html')

def contact (request):
    return render(request, 'shipment/contact.html')