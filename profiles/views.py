from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Worker, Employer, JobPosting
from .serializers import WorkerSerializer, EmployerSerializer, JobPostingSerializer

# Worker Views
class WorkerListView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        workers = Worker.objects.filter(profile_visibility=True).filter(
         Q(availability__icontains=search_query) | Q(certifications__icontains=search_query) | Q(experience__icontains=search_query)
        )
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)
#To give full details of the workers independently

class WorkerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return None

    def get(self, request, pk):
        worker = self.get_object(pk)
        if worker is not None:
            serializer = WorkerSerializer(worker)
            return Response(serializer.data)
        return Response({'message': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        worker = self.get_object(pk)
        if worker is not None:
            serializer = WorkerSerializer(worker, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        worker = self.get_object(pk)
        if worker is not None:
            worker.delete()
            return Response({'message': 'Worker deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)


# Employer Views
class EmployerListView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        employers = Employer.objects.filter(profile_visibility=True).filter(
            Q(company_name__icontains=search_query) | Q(company_description__icontains=search_query)
        )
        serializer = EmployerSerializer(employers, many=True)
        return Response(serializer.data)


class EmployerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Employer.objects.get(pk=pk)
        except Employer.DoesNotExist:
            return None

    def get(self, request, pk):
        employer = self.get_object(pk)
        if employer is not None:
            serializer = EmployerSerializer(employer)
            return Response(serializer.data)
        return Response({'message': 'Employer not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        employer = self.get_object(pk)
        if employer is not None:
            serializer = EmployerSerializer(employer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Employer not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        employer = self.get_object(pk)
        if employer is not None:
            employer.delete()
            return Response({'message': 'Employer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Employer not found'}, status=status.HTTP_404_NOT_FOUND)


# JobPosting Views
class JobPostingListView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        job_postings = JobPosting.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query) |
            Q(skills_required__icontains=search_query) | Q(location__icontains=search_query)
        )
        serializer = JobPostingSerializer(job_postings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobPostingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobPostingDetailView(APIView):
    def get_object(self, pk):
        try:
            return JobPosting.objects.get(pk=pk)
        except JobPosting.DoesNotExist:
            return None

    def get(self, request, pk):
        job_posting = self.get_object(pk)
        if job_posting is not None:
            serializer = JobPostingSerializer(job_posting)
            return Response(serializer.data)
        return Response({'message': 'JobPosting not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        job_posting = self.get_object(pk)
        if job_posting is not None:
            serializer = JobPostingSerializer(job_posting, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'JobPosting not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        job_posting = self.get_object(pk)
        if job_posting is not None:
            job_posting.delete()
            return Response({'message': 'JobPosting deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'JobPosting not found'}, status=status.HTTP_404_NOT_FOUND)
