from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('', views.home, name='home'),
    path('msme_profile/', views.msme_profile, name='msme_profile'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('assistance/', views.assistance, name='assistance'),
    path('business_registration/', views.business_registration, name='business-registration'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('business_advisory/', views.advisory, name='advisory'),
    path('expert_mentor/<str:id_name>', views.expert_mentor, name='expert_mentor'),

    path('contact_person_information/', views.contact_person_information, name='contact_person_information'),
    path('business_information/', views.business_information, name='business_information'),
    path('business_profile/', views.business_profile, name='business_profile'),
    path('business_tracker/', views.business_tracker, name='business_tracker'),
    path('msme_category/', views.msme_category, name='msme_category'),
    path('owner_information/', views.owner_information, name='owner_information'),
    path('financial_structure/', views.financial_structure, name='financial_structure'),
    path('market_access/', views.market_access, name='market_access'),
    path('employment_statistics/', views.employment_statistics, name='employment_statistics'),

]