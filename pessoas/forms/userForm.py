from django import forms
from models import ProfileUser
from django.contrib.auth.models import User

class Userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password','email')
        
