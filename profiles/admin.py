from django.contrib import admin
from .models import Employer,Worker,JobPosting,JobApplication
# Register your models here.
admin.site.register(Employer)
admin.site.register(Worker)
admin.site.register(JobPosting)
admin.site.register(JobApplication)