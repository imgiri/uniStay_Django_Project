from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm 
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods


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
    return render(request, 'unistay/write-review.html', {'form': form})

def about_us(request):
    return render(request, 'unistay/about-us.html')

def contact_us(request):
    return render(request, 'unistay/contact-us.html')

def personal_login(request):
    return render(request, 'unistay/personal-login.html')

def search_results(request):
    return render(request, 'unistay/search-results.html')

def add_accom(request):
    return render(request, 'unistay/add-accom.html')

def my_accoms(request):
    return render(request, 'unistay/my-accoms.html')

def my_profile(request):
    return render(request, 'unistay/my-profile.html')

def faq(request):
    return render(request, 'unistay/faq.html')

"""def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'unistay/signup.html', {'form': form})"""


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            # Handle the marketing opt-in and birthday fields as needed
            # ...
            login(request, user)
            return redirect('index')  # Redirect to the homepage or other appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'unistay/signup.html', {'form': form})


@csrf_protect
def register(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        marketing_emails = request.POST.get('marketing_emails', False)

        # Create user logic here
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            # If you have a user profile or additional settings for marketing_emails, handle them here
            
            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@require_http_methods(["POST"])
def modal_login_view(request):
    # Get credentials from POST request
    email = request.POST.get('email')
    password = request.POST.get('password')

    # Authenticate the user
    user = authenticate(request, username=email, password=password)
    if user is not None:
        # If credentials are correct, login the user
        login(request, user)
        return JsonResponse({'success': True})
    else:
        # If credentials are incorrect
        return JsonResponse({'success': False, 'error': 'Invalid credentials.'})

def logout_user(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'You have been logged out.'})