from django.db import models

# Create your models here.
class BusinessType(models.Model):
    title = models.CharField(max_length=1000)
    details = models.TextField(blank=True, null=True)