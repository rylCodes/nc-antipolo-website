from django.shortcuts import render, redirect
from .models import BusinessType, Mentor, ClientFeedback
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth
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


# Contact Page.
def contact(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        business_name = request.POST['business_name']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        comment = request.POST['comment']
        client_feedback = ClientFeedback(name=name, business_name=business_name, email=email, contact_number=contact_number, comment=comment)
        client_feedback.save()
        messages.success(request, 'Your feedback has been received. Thank you!')
        return redirect('contact')

    context = {
        'page_title': 'Contact',
    }
    return render(request, 'contact.html', context)


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


# MSME Profile Page.
@login_required
def msme_profile(request):
    context = {
        'page_title': 'MSME Profile'
    }
    return render(request, 'msme_profile.html', context)

# Sign Up Page.
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use')
            return redirect('sign_up')
        else:
            msme_account = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            msme_account.save()
            messages.success(request, 'Your account has been registered successfully. You can log-in now')
            return redirect('msme_profile')

    context = {
        'page_title': 'Sign Up'
    }
    return render(request, 'sign_up.html', context)


# Log-In Page.
def login_user(request):
    logout(request) # Clear any existing user session
    response = {'status': 'failed', 'msg': ''} # Create a response dictionary
    email = ''
    password = ''

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active: # Check if the user account is active
                response['status'] = 'success'
            else:
                response['msg'] = 'Incorrect email or password'
        else:
            response['msg'] = 'Incorrect email or password'
    return HttpResponse(json.dumps(response), content_type='application/json') # Return the response as JSON

# Log-Out Function
def logout_user(request):
    logout(request)
    return redirect(request, 'log_in.html')