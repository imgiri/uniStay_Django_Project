from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# User model is already provided by Django, you might extend it using a OneToOneField if needed.

class UserProfile(models.Model):
    # Link UserProfile to Django's User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields as per your ER diagram
    user_type = models.CharField(max_length=20, choices=[('individual', 'Individual'), ('business', 'Business')])

class IndividualUser(models.Model):
    # Link to UserProfile instead of User directly
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    student_id = models.IntegerField()
    year = models.IntegerField()

class BusinessUser(models.Model):
    # Link to UserProfile instead of User directly
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Accommodation(models.Model):
    owner = models.ForeignKey(BusinessUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    facilities = models.TextField()
    accommodation_type = models.CharField(max_length=20, choices=[('university', 'University'), ('private', 'Private')])

class Review(models.Model):
    user = models.ForeignKey(IndividualUser, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now)

class ReviewResponse(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='responses')
    business_user = models.ForeignKey(BusinessUser, on_delete=models.CASCADE)
    response = models.TextField()
    date = models.DateTimeField(default=timezone.now)
