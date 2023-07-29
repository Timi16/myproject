from django.urls import path
from .views import WorkerListView, WorkerDetailView, EmployerListView, EmployerDetailView, JobPostingListView, JobPostingDetailView

urlpatterns = [
    # Worker URLs
    path('workers/', WorkerListView.as_view(), name='worker-list'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),

    # Employer URLs
    path('employers/', EmployerListView.as_view(), name='employer-list'),
    path('employers/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),

    # JobPosting URLs
    path('jobpostings/', JobPostingListView.as_view(), name='jobposting-list'),
    path('jobpostings/<int:pk>/', JobPostingDetailView.as_view(), name='jobposting-detail'),
]
