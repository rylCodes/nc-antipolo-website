from django.shortcuts import render
from .models import BusinessType

# Create your views here.
def home(request):
    context = {
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'page_title': 'About'
    }
    return render(request, 'about.html', context)

def resources(request):
    context = {
        'page_title': 'Resources'
    }
    return render(request, 'resources.html', context)

def assistance(request):
    context = {
        'page_title': 'Assistance'
    }
    return render(request, 'assistance.html', context)

def registration(request):
    business_types = BusinessType.objects.all()
    context = {
        'page_title': 'Business Registration',
        'business_types': business_types
    }
    return render(request, 'registration.html', context)

def contact(request):
    context = {
        'page_title': 'Contact',
    }
    return render(request, 'contact.html', context)

def faqs(request):
    content = {
        'page_title': 'FAQs'
    }
    return render(request, 'faqs.html', content)

def advisory(request):
    content = {
        'page_title': 'Business Advisory'
    }
    return render(request, 'advisory.html', content)
