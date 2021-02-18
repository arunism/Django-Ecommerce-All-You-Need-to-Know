from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from customer.models import Profile

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

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email',
                            widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control', 'placeholder':'Email'}),
                            max_length=100,
                            required=True
                            )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
                    strip=False,
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}),
                    help_text=password_validation.password_validators_help_text_html()
                )
    new_password2 = forms.CharField(
                    strip=False,
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'})
                )



GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not Specified', 'Not Specified'),
)
class ProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=GENDER_CHOICES)
    country = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('Nepal','Nepal'),))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'District'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street'}))

    class Meta:
        model = Profile
        fields = ['phone','gender','country','state','district','street']
