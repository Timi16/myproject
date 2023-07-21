from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.core.validators import EmailValidator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[EmailValidator()]) 
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','username','email','password')

    def create(self, validated_data):
        user = User.objects.create_user(
first_name=validated_data['first_name'],

last_name=validated_data['last_name'],
         username=validated_data['username'],

         password=validated_data['password'],

email=validated_data['email'], 
        )
        return user

#For the Login 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                data['user'] = user
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return data
#password Reset to reset the password
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this email does not exist.')

        if not user.is_active:
            raise serializers.ValidationError('User is not active.')
        return value
        
    def send_password_reset_email(self, user, request):
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = f'http://{request.get_host()}/api/reset-password/{uidb64}/{token}/'

        subject = 'Password Reset'
        message = render_to_string('password_reset_email.html', {
            'user': user,
            'reset_url': reset_url,
        })

        email = EmailMessage(subject, body=message, to=[user.email])
        email.send()
#Password Reset confirmation to change to new password
class PasswordResetConfirmationSerializer(serializers.Serializer):
    new_password = serializers.CharField()

    def validate_new_password(self, value):
        # You can add custom password validation logic here if needed.
        return value