from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
AVAILABILITY_CHOICES = (
    ('full_time', 'Full-Time'),
    ('part_time', 'Part-Time'),
    ('contract', 'Contract'),
)
class Worker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worker_profile')
    skills = models.TextField()
    profile_visibility = models.BooleanField(default=True)  # Public by default
    experience = models.TextField()
    certifications = models.TextField()
    availability = models.CharField(max_length=100,choices=AVAILABILITY_CHOICES)
    #profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Field for Profile Picture
    state = models.CharField(max_length=100, blank=True)  # Field for State
    country = models.CharField(max_length=100, blank=True)  # Field for Country

    # Add any additional fields specific to workers

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer_profile')
    profile_visibility = models.BooleanField(default=True)  # Public by default
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    # Add any additional fields specific to employers

    def __str__(self):
        return self.user.username

class JobPosting(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='job_postings')
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    skills_required = models.TextField()
    location = models.CharField(max_length=100)
    # Add any additional fields specific to job postings

    def __str__(self):
        return self.title
        
class JobApplication(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='job_applications')
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='job_applications')
    application_text = models.TextField()
  #  resume = models.FileField(upload_to='job_applications/resumes/', null=True, blank=True)
    def __str__(self):
        return f"Application for {self.job_posting.title} by {self.worker.user.username}"
