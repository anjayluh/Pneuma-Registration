__author__ = 'LT10'

from django import forms
from django.core.exceptions import ValidationError
from .models import Users
from django.forms import ModelForm
#from django.contrib import auth
from django_password_strength.widgets import PasswordStrengthInput

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    widget = PasswordStrengthInput()
    password = forms.CharField(widget=forms.PasswordStrengthInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def __init__(self, data={}):
        super(UserForm, self).__init__(data=data)
        self.fields['password_again'] = forms.CharField(widget=forms.PasswordStrengthInput)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        if cleaned_data.get('password') != cleaned_data.get('password_again'):
            raise ValidationError('Password Mismatch')
        else:
            return cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username already taken, please choose another')


class UserRegistrationForm(ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="City")
    address = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Address")
    phone_number = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=15)))
    birthdate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Users
        fields = ['city', 'address', 'phone_number', 'birthdate']
