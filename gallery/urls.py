from django.conf import Settings, settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.welcome,name='Gallery'),
    path('search/<category>', views.search_cat, name='search_category'),
    path('temp/', views.search_temp, name='check'),
    path('image/<image_id>/',views.all_images, name='image'),
    path('location/<location_name>/',views.image_location,name = 'location'),
]

if Settings:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)