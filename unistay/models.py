from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=[('individual', 'Individual'), ('business', 'Business')], default='individual')

class IndividualUser(models.Model):

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    student_id = models.IntegerField(default=0)
    year = models.IntegerField(default=1)

class BusinessUser(models.Model):

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
    type = models.CharField(max_length=20, choices=[('university', 'University'), ('private', 'Private')])
    bedrooms = models.IntegerField(default=1)
    budget = models.IntegerField(default=200)
    bathroom_type = models.IntegerField(default=1)


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
