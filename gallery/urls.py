from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path('', views.welcome,name='Gallery'),
    re_path(r'^search/', views.search_cat, name='search_category'),
]