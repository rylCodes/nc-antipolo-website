from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('assistance/', views.assistance, name='assistance'),
    path('business_registration/', views.registration, name='registration'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('business_advisory/', views.advisory, name='advisory'),
    path('expert_mentor/<str:id_name>', views.expert_mentor, name='expert_mentor'),
    
]