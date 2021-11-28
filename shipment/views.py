from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from shipment.forms import ItemTrackForm, ContactForm
from shipment.models import ItemDetail
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def index (request):
    return render(request, 'shipment/index.html', {'title': 'home'})

def about (request):
    return render(request, 'shipment/about.html', {'title': 'about'})

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
        'item': item,
        'title': 'tracking'
    }
    return render(request, 'shipment/track.html', context)

def services (request):
    return render(request, 'shipment/services.html', {'title': 'services'})

def contact (request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['sdelivery@biz.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header')
            messages.success(request, f"message have been sent successfully")
            return redirect("contact")
        else:
            print("Failed form submission")
    

    context = {
        'form': form,
        'title': 'contact Us'
    }                           
    return render(request, 'shipment/contact.html', context)