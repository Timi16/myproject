from rest_framework import serializers
from .models import Worker, Employer, JobPosting,JobApplication

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        exclude = ('user',)

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        exclude = ('user',)
class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        exclude=('employer',)

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'