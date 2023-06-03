from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('assistance/', views.assistance, name='assistance'),
    path('business_registration/', views.business_registration, name='business_registration'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
]