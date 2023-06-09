from django.shortcuts import render
from .models import BusinessType, Expert
from django.core.paginator import Paginator

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


def expert_mentor(request, id_name):
    mentors = Expert.objects.get(id_name=id_name)
    expertise = mentors.expertise
    related_mentors = Expert.objects.filter(expertise__contains=expertise).exclude(id_name=id_name)
    
    content = {
        'mentors': mentors,
        'related_mentors': related_mentors,
        'page_title': 'Expert Mentors'
    }
    return render(request, 'expert_mentor.html', content)


