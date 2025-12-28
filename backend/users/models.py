from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extended user profile for Nyota Catalyst program participants"""
    
    # Application Status Choices
    STATUS_PENDING = 'pending'
    STATUS_SEEKING_SUPPORT = 'seeking_support'
    STATUS_ENROLLED = 'enrolled'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Applied - Pending Approval'),
        (STATUS_SEEKING_SUPPORT, 'Seeking Support'),
        (STATUS_ENROLLED, 'Enrolled'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Profile Picture
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True,
        help_text="Profile picture"
    )
    
    # Additional Information
    background = models.TextField(
        max_length=2000,
        blank=True,
        help_text="Tell us about your background, experience, and what drives you as an entrepreneur (max 2000 characters)"
    )
    project_description = models.TextField(
        max_length=3000,
        blank=True,
        help_text="Describe your project, the problem it solves, and your vision (max 3000 characters)"
    )
    
    # Application Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        help_text="Current status in the Nyota Catalyst program"
    )
    
    # Enrollment Details
    enrollment_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date when the participant was enrolled in the program"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def is_enrolled(self):
        return self.status == self.STATUS_ENROLLED
    
    @property
    def is_pending(self):
        return self.status == self.STATUS_PENDING
    
    @property
    def is_seeking_support(self):
        return self.status == self.STATUS_SEEKING_SUPPORT

