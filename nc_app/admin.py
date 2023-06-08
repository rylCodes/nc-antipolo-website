from django.contrib import admin
from .models import BusinessType, Expert, Education, Experience, Detail

# Register your models here.
admin.site.register(BusinessType)
admin.site.register(Expert)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Detail)
