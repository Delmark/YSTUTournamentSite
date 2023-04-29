from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import News, Player, PlayerStats, Team

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content')
