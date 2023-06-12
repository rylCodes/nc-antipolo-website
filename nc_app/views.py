from django.shortcuts import render, redirect
from .models import BusinessType, Expert, Specialization, ClientFeedback
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages

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
        name = request.POST.get('fullname')
        business_name = request.POST.get('business_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')
        client_feedback = ClientFeedback(name=name, business_name=business_name, email=email, contact_number=contact_number, message=message)
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
    experts = Expert.objects.all()
    filter_value = request.GET.get('filter')
    #experts_per_page = 8
    #paginator = Paginator(experts, experts_per_page)

    if filter_value:
        experts = experts.filter(expertise__contains=filter_value)

    content = {
        'page_title': 'Business Advisory',
        'experts': experts,
        'selected_filter': filter_value
    }
    return render(request, 'advisory.html', content)


# Expert Mentor Page.
def expert_mentor(request, id_name):
    mentor = Expert.objects.get(id_name=id_name)
    specializations = mentor.expertises.values_list('field', flat=True)  # Get the list of specializations for the mentor
    related_mentors = Expert.objects.filter(expertises__field__in=specializations).exclude(id_name=id_name).distinct()
    
    content = {
        'mentor': mentor,
        'related_mentors': related_mentors,
        'page_title': 'Expert Mentors'
    }
    return render(request, 'expert_mentor.html', content)

def msme_profile(request):
    context = {
        'page_title': 'MSME Profile'
    }
    return render(request, 'msme_profile.html', context)

def sign_up(request):
    context = {
        'page_title': 'Sign Up'
    }
    return render(request, 'sign_up.html', context)





