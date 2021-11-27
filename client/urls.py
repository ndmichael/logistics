from django.urls import path
from .views import dashboard



urlpatterns = [
    path('<str:username>', dashboard, name="client-dashboard" ),
]