from django.urls import path
from form_app import views

urlpatterns=[
    path('home/',views.registration)
]