#created for testing purpose

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, Accommodation

class ReviewForm(forms.ModelForm):
    accommodation = forms.ModelChoiceField(
        queryset=Accommodation.objects.all(),
        empty_label="Select Accommodation",
        label="Accommodation",
        required=True
    )

    class Meta:
        model = Review
        fields = ['accommodation', 'rating', 'review']
    
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    marketing_opt_in = forms.BooleanField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'marketing_opt_in')

    
