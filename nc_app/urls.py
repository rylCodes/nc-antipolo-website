from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('', views.home, name='home'),
    path('msme_profiling/', views.msme_profiling, name='msme_profiling'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('assistance/', views.assistance, name='assistance'),
    path('business_registration/', views.registration, name='registration'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('business_advisory/', views.advisory, name='advisory'),
    path('expert_mentor/<str:id_name>', views.expert_mentor, name='expert_mentor'),
    path('msme_profile/', views.msme_profile, name='msme_profile'),
    path('log_in/', views.login_user, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    
]