from django.forms import TextInput
from django.utils.translation import ugettext as _
from django import forms

__author__ = 'n.nikolic'

class SignUpForm(forms.Form):
    """
    Email sing-up form for lander page
    """
    #csrfmiddlewaretoken = forms.HiddenInput()
    email = forms.EmailField(label=_('Your Email'))
    name = forms.CharField(max_length=100, label=_('Your Name'))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = TextInput(attrs={
            'id': 'emailfield',
            'class': 'form-control',
            'name': 'emailfield',
            'placeholder': _('your@mail.com')})
        self.fields['name'].widget = TextInput(attrs={
            'id': 'namefield',
            'class': 'form-control',
            'name': 'namefield',
            'placeholder': _('Enter your name')})