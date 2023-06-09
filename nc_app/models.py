from django.db import models

# Create your models here.
class BusinessType(models.Model):
    title = models.CharField(max_length=1000)
    details = models.TextField(blank=True, null=True)


class Expert(models.Model):
    name = models.CharField(max_length=200)
    id_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to='experts', blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
 
    def __str__(self):
        return f"{self.name}"


# Using ForeignKey Expert
class Education(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
 
    def __str__(self):
        return f"{self.expert.name} - Education {self.pk}"


class Experience(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='experiences')
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.expert.name} - Experience {self.pk}"


class Detail(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()

    def __str__(self):
        return f"{self.expert.name} - Detail {self.pk}"
    
    #class Meta:
        #ordering = ['id']
