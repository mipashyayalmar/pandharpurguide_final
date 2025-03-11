# This is the urls.py file for defining URL patterns in the Django app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advertisement/', views.advertisement, name='advertisement'),
]
