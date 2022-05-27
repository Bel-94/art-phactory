from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path('', views.welcome,name='Gallery'),
    re_path(r'^search/', views.search_cat, name='search_category'),
    re_path('^image/(?P<image_id>\d+)/$',views.all_images, name='image'),
    re_path(r'^location/(?P<location_name>\w+)',views.image_location,name = 'location'),
]