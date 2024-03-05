#created for testing purpose

from django import forms


class ReviewForm(forms.Form):
    accommodation_name = forms.CharField(label='Accommodation Name', max_length=100)
    rating = forms.ChoiceField(label='Select your rating', choices=[(x, x) for x in range(1, 6)])
    review = forms.CharField(widget=forms.Textarea, label='Your Review')
    photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Attach Photos')
    
