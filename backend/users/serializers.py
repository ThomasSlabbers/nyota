from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import UserProfile


class FoundersListSerializer(serializers.ModelSerializer):
    """Public serializer for listing founders"""
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    profile_picture_url = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'profile_picture_url',
            'background', 
            'project_description', 
            'status',
            'status_display',
            'enrollment_date'
        ]
    
    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile_picture.url)
        return None


class UserProfileSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ['background', 'project_description', 'status', 'enrollment_date', 'profile_picture', 'profile_picture_url']
        read_only_fields = ['status', 'enrollment_date', 'profile_picture_url']
    
    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile_picture.url)
        return None


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user profile information"""
    class Meta:
        model = UserProfile
        fields = ['background', 'project_description']
    
    def validate_background(self, value):
        if len(value) > 2000:
            raise serializers.ValidationError("Background cannot exceed 2000 characters.")
        return value
    
    def validate_project_description(self, value):
        if len(value) > 3000:
            raise serializers.ValidationError("Project description cannot exceed 3000 characters.")
        return value


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        read_only_fields = ['id']


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user information and profile"""
    background = serializers.CharField(required=False, allow_blank=True, max_length=2000)
    project_description = serializers.CharField(required=False, allow_blank=True, max_length=3000)
    profile_picture = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'background', 'project_description', 'profile_picture']
    
    def update(self, instance, validated_data):
        # Extract profile fields
        background = validated_data.pop('background', None)
        project_description = validated_data.pop('project_description', None)
        profile_picture = validated_data.pop('profile_picture', None)
        
        # Update user fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        
        # Update or create profile
        profile, _ = UserProfile.objects.get_or_create(user=instance)
        if background is not None:
            profile.background = background
        if project_description is not None:
            profile.project_description = project_description
        if profile_picture is not None:
            profile.profile_picture = profile_picture
        profile.save()
        
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Confirm Password')
    background = serializers.CharField(required=False, allow_blank=True, max_length=2000)
    project_description = serializers.CharField(required=False, allow_blank=True, max_length=3000)
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'background', 'project_description', 'profile_picture']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        background = validated_data.pop('background', '')
        project_description = validated_data.pop('project_description', '')
        profile_picture = validated_data.pop('profile_picture', None)
        
        user = User.objects.create_user(**validated_data)
        
        # Create profile with picture
        UserProfile.objects.create(
            user=user,
            background=background,
            project_description=project_description,
            profile_picture=profile_picture,
            status=UserProfile.STATUS_PENDING
        )
        
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')

        user = None
        try:
            if '@' in username_or_email:
                user = User.objects.get(email=username_or_email)
                username = user.username
            else:
                username = username_or_email
        except User.DoesNotExist:
            username = username_or_email

        user = authenticate(username=username, password=password)

        if user is None:
            from rest_framework_simplejwt.exceptions import AuthenticationFailed
            raise AuthenticationFailed('No active account found with the given credentials')

        data = {}
        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

