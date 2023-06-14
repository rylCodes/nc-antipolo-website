from django.contrib import admin
from .models import BusinessType, Mentor, MentorEducation, MentorExperience, MentorBiography, ClientFeedback, MentorSpecialization

# Register your models here.
admin.site.register(BusinessType)
admin.site.register(Mentor)
admin.site.register(MentorEducation)
admin.site.register(MentorExperience)
admin.site.register(MentorBiography)
admin.site.register(ClientFeedback)
admin.site.register(MentorSpecialization)