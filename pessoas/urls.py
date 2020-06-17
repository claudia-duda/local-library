from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/' , views.register, name='register'), 
]