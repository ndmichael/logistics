from django.shortcuts import render

# Create your views here.

def dashboard(request, username):
    context = {}
    return render(request, 'account/user/dashboard.html', context)
