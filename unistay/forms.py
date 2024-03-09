#created for testing purpose

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(forms.Form):
    accommodation_name = forms.CharField(label='Accommodation Name', max_length=100)
    rating = forms.ChoiceField(label='Select your rating', choices=[(x, x) for x in range(1, 6)])
    review = forms.CharField(widget=forms.Textarea, label='Your Review')
    photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False, label='Attach Photos')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    
