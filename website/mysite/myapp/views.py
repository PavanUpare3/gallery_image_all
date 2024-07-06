from django.shortcuts import render
from .models import Image

def index(request):
    return render(request, 'index.html')

def singleGallery(request):
    return render(request, 'gallery-single.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def galler(request):
    fm= Image.objects.all()
    return render(request, 'gallery.html', {"form": fm})

def galldemo(request):
    fm= Image.objects.all()
    return render(request, 'gallery_demo.html', {"form": fm})
