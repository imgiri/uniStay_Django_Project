from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm 
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Accommodation
from .forms import ReviewForm
from .models import Review, IndividualUser, UserProfile
from functools import wraps
from .decorators import login_required_ajax
from django.utils import timezone


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

@login_required  # This decorator ensures only logged-in users can access the profile
def view_profile(request):
    return render(request, 'unistay/my-profile.html', {'user': request.user})

def faq(request):
    return render(request, 'unistay/faq.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            
            login(request, user)
            return redirect('index')  # Redirect to the homepage
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


def accommodation_list(request):
    # Get filter values from the request
    type_filter = request.GET.get('type')
    bedrooms_filter = request.GET.get('bedrooms')
    budget_filter = request.GET.get('budget')
    bathroom_type_filter = request.GET.get('bathroom_type')
    
    # Start with all records
    accommodations = Accommodation.objects.all()
    
    # Render the filtered queryset to a template
    return render(request, 'unistay/accommodation-list.html', {'accommodations': accommodations})

def write_review(request):
    accommodations = Accommodation.objects.all()

    context = {
        'accommodations': accommodations,
    }

    if request.method == 'POST':
        accommodation_id = request.POST.get('accommodation')
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        accommodation = get_object_or_404(Accommodation, id=accommodation_id)

        # Check for UserProfile existence and create if necessary
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Now safely get or create the IndividualUser linked to that UserProfile
        individual_user, created = IndividualUser.objects.get_or_create(user_profile=user_profile)


        # Create a new Review instance and save it
        review_instance = Review(
            user=individual_user,
            accommodation=accommodation,
            rating=rating,
            review=review,
            date=timezone.now()  #set the review date to now
        )
        
        review_instance.save()

    
        # Redirect to a index page 
        return redirect('index')  

    return render(request, 'unistay/write-review.html', context)

#@login_required_ajax
def write_a_review(request):
    """if request.method == 'POST':
        form = ReviewForm(request.POST)
        console.log("inside here")
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user  # Set the user to the currently logged-in user
            new_review.save()
            return redirect('review_thank_you')  # Redirect to a thank-you page or similar
    else:
        form = ReviewForm()"""
    
    return render(request, 'unistay/write-a-review.html')

