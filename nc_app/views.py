from django.shortcuts import render, redirect
from .models import BusinessType, Mentor, ClientFeedback
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse

# Sign Up Page.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use')
                return redirect('signup')
            else:
                new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                new_user.save()
                messages.success(request, 'Your account has been registered successfully. You can log-in now')
                return redirect('user_login')
        else:
            messages.error(request, 'Password is not the same')
            return redirect('signup')
    else:
        context = {
        'page_title': 'Sign Up'
        }
        return render(request, 'signup.html', context)


# Login User Page.
def user_login(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('msme_profile')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('user_login')
    else:
        return render(request, 'user_login.html')

# Logout Function
def user_logout(request):
    logout(request)
    return redirect('user_login')


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
        address = request.POST['address']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        comment = request.POST['comment']
        client_feedback = ClientFeedback(name=name, business_name=business_name, email=email, contact_number=contact_number, comment=comment, address=address)
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



# MSME Profile Page.
@login_required
def msme_profile(request):
    context = {
        'page_title': 'MSME Profile'
    }
    return render(request, 'msme_profile.html', context)

@login_required
def contact_person_information(request):
    context = {
        'page_title': 'Contact Person Information'
    }
    return render(request, 'msme_profile/contact_person_information.html', context)

@login_required
def business_information(request):
    context = {
        'page_title': 'Business Registration / Contact Information'
    }
    return render(request, 'msme_profile/business_information.html', context)

@login_required
def business_profile(request):
    context = {
        'page_title': 'Business Profile'
    }
    return render(request, 'msme_profile/business_profile.html', context)

@login_required
def business_tracker(request):
    context = {
        'page_title': 'Business Tracker'
    }
    return render(request, 'msme_profile/business_tracker.html', context)

@login_required
def msme_category(request):
    context = {
        'page_title': 'MSME Category'
    }
    return render(request, 'msme_profile/msme_category.html', context)

@login_required
def owner_information(request):
    context = {
        'page_title': 'Owner Information'
    }
    return render(request, 'msme_profile/owner_information.html', context)

@login_required
def financial_structure(request):
    context = {
        'page_title': 'Financial Structure'
    }
    return render(request, 'msme_profile/financial_structure.html', context)

@login_required
def market_access(request):
    context = {
        'page_title': 'Market Access'
    }
    return render(request, 'msme_profile/market_access.html', context)

@login_required
def employment_statistics(request):
    context = {
        'page_title': 'Employment Statistics'
    }
    return render(request, 'msme_profile/employment_statistics.html', context)
