from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserProfile
from .serializers import (
    RegisterSerializer, 
    UserSerializer, 
    UserUpdateSerializer,
    CustomTokenObtainPairSerializer,
    FoundersListSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    """View for retrieving and updating user information"""
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return UserSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_object(self):
        return self.request.user


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class HealthCheckView(APIView):
    """Health check endpoint"""
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({
            'status': 'ok',
            'message': 'API is running successfully!',
            'version': '1.0.0'
        })


class FoundersListView(generics.ListAPIView):
    """View for listing all founders with optional status filtering"""
    serializer_class = FoundersListSerializer
    permission_classes = (permissions.AllowAny,)
    
    def get_queryset(self):
        queryset = UserProfile.objects.select_related('user').all()
        
        # Filter by status if provided
        status = self.request.query_params.get('status', None)
        if status:
            if status == 'all':
                # Show all founders except pending (only seeking_support and enrolled)
                queryset = queryset.exclude(status=UserProfile.STATUS_PENDING)
            elif status in ['pending', 'seeking_support', 'enrolled']:
                queryset = queryset.filter(status=status)
        else:
            # Default: exclude pending applications
            queryset = queryset.exclude(status=UserProfile.STATUS_PENDING)
        
        return queryset.order_by('-created_at')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

