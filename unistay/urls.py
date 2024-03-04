from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write-review/', views.write_review, name='write_review'),
]