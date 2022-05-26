from django.shortcuts import render
from .models import Location, Image, Category
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    pass

def all_images(request,image_id):
    pass

def image_location(request,location_name):
    pass

def search_cat(request):
    pass
