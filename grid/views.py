from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Location, Category, Editor

# Create your views here.
def gallery(request):
    images = Image.get_images()
    locations = Location.objects.all()
    return render(request, 'gallery.html',{"images":images, "locations":locations})
