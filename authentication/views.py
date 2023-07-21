from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer,PasswordResetRequestSerializer,PasswordResetConfirmationSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
# Create your views here.

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Registration successful. Welcome, {}!'.format(user.username)
            })
        else:
            return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful. Welcome, {}!'.format(user.username)
            })
        else:
            return Response({
                'error': 'Invalid credentials. Please try again.'
            }, status=401)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'detail': 'Logout successful.'})
            except Exception as e:
                return Response({'detail': str(e)}, status=400)
        else:
            return Response({'detail': 'Refresh token not provided.'}, status=400)

class PasswordResetRequestView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.validated_data['email'])
        serializer.send_password_reset_email(user, request)

        return Response({'success': 'Password reset email sent.'}, status=status.HTTP_200_OK)
class PasswordResetConfirmationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, uidb64, token):
        serializer = PasswordResetConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            new_password = serializer.validated_data['new_password']
            user.set_password(new_password)
            user.save()
            return Response({'success': 'Password reset successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)