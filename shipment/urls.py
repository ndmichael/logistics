from django.urls import path
from shipment import views as shipment_views

app_name = 'shop'

urlpatterns = [
    path('', shipment_views.index, name='shipment_index'),
    path('about/', shipment_views.about, name='shipment_about'),
    path('<int:id>/<slug:slug>/', shipment_views.contact, name='shipment_contact'),   

]