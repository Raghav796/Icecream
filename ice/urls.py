from django.contrib import admin
from django.urls import path
from ice import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("scoops", views.scoops, name='scoops'),
    path("bars", views.bars, name='bars'),
    path("cones", views.cones, name='cones'),
    path("tubs", views.tubs, name='tubs'),
    
]
