from django.db import models

# Create your models here.
class BusinessType(models.Model):
    title = models.CharField(max_length=1000)
    details = models.TextField(blank=True, null=True)

from django.db import models

class Expert(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to='experts', blank=True, null=True)

class Education(models.Model):
    mentor = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    # Other fields specific to education

class Experience(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='experiences')
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    # Other fields specific to experience

class Detail(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(max_length=200)
    # Other fields specific to details
