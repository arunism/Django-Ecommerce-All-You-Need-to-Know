from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import password_validation

class UserRegisterationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                required=True
                                )
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                required=True
                                )
    username = forms.CharField(label='Username',
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                required=True
                                )
    email = forms.CharField(label='Email',
                                widget=forms.EmailInput(attrs={'class':'form-control'}),
                                required=True
                                )
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                required=True
                                )
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                required=True
                                )
                                

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
                    strip=False,
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Current Password'})
                )
    new_password1 = forms.CharField(
                    strip=False,
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}),
                    help_text=password_validation.password_validators_help_text_html()
                )
    new_password2 = forms.CharField(
                    strip=False,
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'})
                )
