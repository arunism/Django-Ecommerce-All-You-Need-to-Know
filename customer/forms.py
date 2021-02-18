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
STATE_CHOICES = (
    ('Province No. 1', 'Province No. 1'),
    ('Province No. 2', 'Province No. 2'),
    ('Province No. 3', 'Province No. 3'),
    ('Province No. 4', 'Province No. 4'),
    ('Province No. 5', 'Province No. 5'),
    ('Province No. 6', 'Province No. 6'),
    ('Province No. 7', 'Province No. 7'),
)
class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=GENDER_CHOICES, required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone *'}), required=True)
    country = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('Nepal','Nepal'),), required=True)
    state = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=STATE_CHOICES, required=True)
    district = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'District *'}), required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City *'}), required=True)
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street *'}), required=True)
    building_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Building No'}), required=False)
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}), required=False)

    class Meta:
        model = Profile
        fields = ['gender','phone','country','state','district','city','street','building_no','zip_code']
