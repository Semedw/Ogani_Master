from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from user.models import MyUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Password'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Confirm Password'}))

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'address', 'password')
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Last Name'}),
            'username' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Username'}),
            'email' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'E-mail'}),
            'address' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Address'}),
            'password' : forms.PasswordInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Password'}),
        }
        

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['address'].label = ''
        self.fields['password'].label = ''
        self.fields['confirm_password'].label = ''



    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords does not match")
        return cleaned_data

    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError("Password must be contain at least 8 characters")
        
        return password
    

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        
        return username
    

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Password'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.help_text = ''
            field.label = ''