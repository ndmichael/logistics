from django.urls import path
from shipment import views as shipment_views

# app_name = 'shop'

urlpatterns = [
    path('', shipment_views.index, name='shipment_index'),
    path('about/', shipment_views.about, name='shipment_about'),
    path('conact/', shipment_views.contact, name='shipment_contact'), 
    path('tracking/', shipment_views.track, name='shipment_track'),
    path('service/', shipment_views.services, name='shipment_service'),  

]