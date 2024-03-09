from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write-review/', views.write_review, name='write_review'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('personal-login/', views.personal_login, name='personal_login'),
    path('signup/', views.signup, name='signup'),
]

