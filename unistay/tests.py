from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile, IndividualUser, BusinessUser, Accommodation, Review, ReviewResponse
from .forms import ReviewForm, CustomUserCreationForm
from django.urls import reverse

# Create your tests here.

class IndividualUserModelTest(TestCase):
    def test_individual_user_creation(self):
        user = User.objects.create(username='John')
        user_profile = UserProfile.objects.create(user=user, user_type='individual')
        individual_user = IndividualUser.objects.create(user_profile=user_profile, student_id=123456, year=2023)
        self.assertEqual(individual_user.student_id, 123456)

class BusinessUserModelTest(TestCase):
    def test_business_user_creation(self):
        user = User.objects.create(username='IQ')
        user_profile = UserProfile.objects.create(user=user, user_type='business')
        business_user = BusinessUser.objects.create(user_profile=user_profile, business_name='IQ', business_type='Property Block', location='11 University Gardens')
        self.assertEqual(business_user.business_type, 'Property Block')

class AccommodationModelTest(TestCase):
    def test_accommodation_creation(self):
        user = User.objects.create(username='IQ')
        user_profile = UserProfile.objects.create(user=user, user_type='business')
        business_user = BusinessUser.objects.create(user_profile=user_profile, business_name='IQ', business_type='Property Block', location='11 University Gardens')
        accommodation = Accommodation.objects.create(owner=business_user, name='Havannah House', location='Room 220, BlockA, 16 Havannah House', description='This is a student accommodation which is a studio.', price=190.00, facilities='gym, study room and reception', accommodation_type='university')
        self.assertEqual(accommodation.location, 'Room 220, BlockA, 16 Havannah House')

class ReviewModelTest(TestCase):
    def test_review_creation(self):
        user = User.objects.create(username='John')
        user_profile = UserProfile.objects.create(user=user, user_type='individual')
        individual_user = IndividualUser.objects.create(user_profile=user_profile, student_id=123456, year=2023)
        business_user = BusinessUser.objects.create(user_profile=user_profile, business_name='IQ', business_type='Property Block', location='11 University Gardens')
        accommodation = Accommodation.objects.create(owner=business_user, name='Havannah House', location='Room 220, BlockA, 16 Havannah House', description='This is a student accommodation which is a studio.', price=190.00, facilities='gym, study room and reception', accommodation_type='university')
        review = Review.objects.create(user=individual_user, accommodation=accommodation, rating=4.5, review='Great experience!')
        self.assertEqual(review.rating, 4.5)

class ReviewResponseModelTest(TestCase):
    def test_review_response_creation(self):
        user = User.objects.create(username='IQ')
        user_profile = UserProfile.objects.create(user=user, user_type='business')
        business_user = BusinessUser.objects.create(user_profile=user_profile, business_name='IQ', business_type='Property Block', location='11 University Gardens')
        user2 = User.objects.create(username='John')
        user_profile2 = UserProfile.objects.create(user=user2, user_type='individual')
        individual_user = IndividualUser.objects.create(user_profile=user_profile2, student_id=123456, year=2023)
        business_user2 = BusinessUser.objects.create(user_profile=user_profile2, business_name='IQ', business_type='Property Block', location='11 University Gardens')
        accommodation = Accommodation.objects.create(owner=business_user, name='Havannah House', location='Room 220, BlockA, 16 Havannah House', description='This is a student accommodation which is a studio.', price=190.00, facilities='gym, study room and reception', accommodation_type='university')
        review = Review.objects.create(user=individual_user, accommodation=accommodation, rating=4.5, review='Great experience!')
        review_response = ReviewResponse.objects.create(review=review, business_user=business_user2, response='Thank you for your review.')
        self.assertEqual(review_response.response, 'Thank you for your review.')


class ReviewFormTest(TestCase):
    def test_review_form_valid_data(self):
        form_data = {
            'accommodation_name': 'Test Accommodation',
            'rating': '5',
            'review': 'Test review content',
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_data(self):
        form_data = {
            'rating': '5',
            'review': 'Test review content',
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormTest(TestCase):
    def test_custom_user_creation_form_valid_data(self):
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'marketing_opt_in': True,
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_data(self):
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalidemail',  # Invalid email format
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'marketing_opt_in': True,
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/index.html')

    def test_write_review_view_GET(self):
        response = self.client.get(reverse('write_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/write-review.html')
        self.assertIsInstance(response.context['form'], ReviewForm)

    def test_write_review_view_POST_valid_form(self):
        data = {'accommodation_name': 'Test Accommodation', 'rating': '5', 'review': 'Test review content'}
        response = self.client.post(reverse('write_review'), data)
        self.assertEqual(response.status_code, 302)  # Redirects to index upon successful form submission

    def test_about_us_view(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/about-us.html')

    def test_contact_us_view(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/contact-us.html')

    def test_personal_login_view(self):
        response = self.client.get(reverse('personal_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/personal-login.html')

    def test_search_results_view(self):
        response = self.client.get(reverse('search_results'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/search-results.html')

    def test_add_accom_view(self):
        response = self.client.get(reverse('add_accom'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/add-accom.html')

    def test_my_accoms_view(self):
        response = self.client.get(reverse('my_accoms'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/my-accoms.html')

    def test_my_profile_view(self):
        response = self.client.get(reverse('my_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/my-profile.html')

    def test_faq_view(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/faq.html')

    def test_signup_view_GET(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unistay/signup.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_signup_view_POST_valid_form(self):
        data = {'username': 'testuser', 'first_name': 'Test', 'last_name': 'User', 'email': 'test@example.com', 'password1': 'testpassword123', 'password2': 'testpassword123', 'marketing_opt_in': True}
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)  # Redirects to index upon successful form submission

    def test_signup_view_POST_invalid_form(self):
        data = {}  # Invalid form data
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)  # Form submission fails, returns to signup page

    def test_register_view_POST_valid_data(self):
        data = {'first_name': 'Test', 'last_name': 'User', 'email': 'test@example.com', 'password': 'testpassword123', 'marketing_emails': 'true'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Registration successful, returns status 200