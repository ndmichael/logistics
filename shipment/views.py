from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from shipment.forms import ItemTrackForm, ContactForm
from shipment.models import ItemDetail

# Create your views here.


def index (request):
    return render(request, 'shipment/index.html')

def about (request):
    return render(request, 'shipment/about.html')

def track_item (request):
    form = ItemTrackForm()
    item=None
    if 'q' in request.POST:
        form = ItemTrackForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q']
            item = ItemDetail.objects.filter(item_code=q).first()
            
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'shipment/track.html', context)

def services (request):
    return render(request, 'shipment/services.html')

def contact (request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print("Success")
            messages.success(request, f"Recipe for {name} added successfully")
            return redirect("shipment_index")
        else:
            print("Failed form submission")
    

    context = {
        'form': form
    }                           
    return render(request, 'shipment/contact.html', context)