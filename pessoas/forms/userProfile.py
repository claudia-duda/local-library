from django import forms
from ..models import ProfileUser 
class UserProfileInfo(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields('name','profile_pic','allbooks')