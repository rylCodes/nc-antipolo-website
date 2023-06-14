from django.db import models

# Registration Page.
class BusinessType(models.Model):
    title = models.CharField(max_length=1000)
    details = models.TextField(blank=True, null=True)


# Advisory and Expert Mentor Page.
class Mentor(models.Model):
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


class MentorEducation(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
 
    def __str__(self):
        return f"{self.mentor.name} - Education {self.pk}"


class MentorExperience(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='experiences')
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.mentor.name} - Experience {self.pk}"


class MentorBiography(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()

    def __str__(self):
        return f"{self.mentor.name} - Detail {self.pk}"
    #class Meta:
        #ordering = ['id']

class MentorSpecialization(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='expertises')
    field = models.CharField(max_length=200)


# Contact Page.
class ClientFeedback(models.Model):
    name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    contact_number = models.IntegerField(max_length=11)
    comment = models.TextField()


# Sign-Up Page.
class SignUp(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
