from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Member

__author__ = 'n.nikolic'

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('website', 'picture')