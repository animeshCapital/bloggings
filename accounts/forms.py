from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # def clean_username(self):
        #     username = self.cleaned_data.get('username')
        #     if not admin in username:
        #         raise forms.validationError('Enter Username')
        #     else:
        #         return username

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'phone_no']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not admin in username:
            raise forms.validationError('Enter Username')
        else:
            return username


