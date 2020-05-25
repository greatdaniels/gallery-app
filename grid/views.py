from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Location, Category, Editor

# Create your views here.
def gallery(request):
    images = Image.get_images()
    locations = Location.objects.all()
    return render(request, 'gallery.html',{"images":images, "locations":locations})

def location_filter(request, location):
    locations = Location.objects.all()
    images = Image.objects.filter(location__id = location)
    title = 'Location Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})