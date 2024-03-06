from django.shortcuts import render, redirect
from .forms import ReviewForm

# Create your views here.

def index(request):
    # Your logic here
    return render(request, 'unistay/index.html')

def write_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'unistay/write_review.html', {'form': form})

def about_us(request):
    return render(request, 'unistay/about-us.html')

def contact_us(request):
    return render(request, 'unistay/contact-us.html')

def personal_login(request):
    return render(request, 'unistay/personal-login.html')
