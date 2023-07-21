from django.urls import path
from authentication.views import RegisterView,LoginView,LogoutView,PasswordResetRequestView,PasswordResetConfirmationView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
   path('api/login/', LoginView.as_view(), name='login'),
   path("api/logout/",LogoutView.as_view(),name="logout"),
   path('api/forget/', PasswordResetRequestView.as_view(), name='forget'),
   path('api/reset-password/<str:uidb64>/<str:token>/', PasswordResetConfirmationView.as_view(), name='password-reset-confirm')
]
