from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')
