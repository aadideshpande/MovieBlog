from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #whenever the form validates, we create a new user
        fields = ['username', 'email', 'password1', 'password2']    #these are to be shown on the form


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User  # images are in Profile model , so we need to do it differently
        fields = ['username', 'email'] 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']