from django.db import models

# Registration Page.
class BusinessType(models.Model):
    title = models.CharField(max_length=1000)
    details = models.TextField(blank=True, null=True)



# Advisory and Expert Mentor Page.
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

class Specialization(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='expertises')
    field = models.CharField(max_length=200)



# Contact Page.
class ClientFeedback(models.Model):
    name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=200)
    message = models.TextField()