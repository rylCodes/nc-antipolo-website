from django.shortcuts import render, redirect
from .models import BusinessType, Mentor, ClientFeedback
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
import json

# Home Page.
def home(request):
    context = {
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)


# About Page.
def about(request):
    context = {
        'page_title': 'About'
    }
    return render(request, 'about.html', context)


# Resources Page.
def resources(request):
    context = {
        'page_title': 'Resources'
    }
    return render(request, 'resources.html', context)


# Assistance Page.
def assistance(request):
    context = {
        'page_title': 'Assistance'
    }
    return render(request, 'assistance.html', context)


# Registration Page.
def registration(request):
    business_types = BusinessType.objects.all()
    context = {
        'page_title': 'Business Registration',
        'business_types': business_types
    }
    return render(request, 'registration.html', context)


# Contact Us Page.
def contact_us(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        business_name = request.POST['business_name']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        comment = request.POST['comment']
        client_feedback = ClientFeedback(name=name, business_name=business_name, email=email, contact_number=contact_number, comment=comment)
        client_feedback.save()
        messages.success(request, 'Your feedback has been received. Thank you!')
        return redirect('contact_us')

    context = {
        'page_title': 'Contact Us',
    }
    return render(request, 'contact_us.html', context)


# FAQs Page.
def faqs(request):
    content = {
        'page_title': 'FAQs'
    }
    return render(request, 'faqs.html', content)


# Advisory Page.
def advisory(request):
    mentors = Mentor.objects.all()
    filter_value = request.GET.get('filter')
    #mentors_per_page = 8
    #paginator = Paginator(mentors, mentors_per_page)

    if filter_value:
        mentors = mentors.filter(expertise__contains=filter_value)

    content = {
        'page_title': 'Business Advisory',
        'mentors': mentors,
        'selected_filter': filter_value
    }
    return render(request, 'advisory.html', content)


# Expert Mentor Page.
def expert_mentor(request, id_name):
    mentor = Mentor.objects.get(id_name=id_name)
    specializations = mentor.expertises.values_list('field', flat=True)  # Get the list of specializations for the mentor
    related_mentors = Mentor.objects.filter(expertises__field__in=specializations).exclude(id_name=id_name).distinct()
    
    content = {
        'mentor': mentor,
        'related_mentors': related_mentors,
        'page_title': 'Expert Mentors'
    }
    return render(request, 'expert_mentor.html', content)
