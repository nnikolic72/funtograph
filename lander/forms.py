from django.forms import TextInput
from django.utils.translation import ugettext as _
from django.forms import ModelForm

from .models import Lander
__author__ = 'n.nikolic'

class SignUpForm(ModelForm):
    """
    Email sing-up form for lander page
    """
    class Meta:
        model = Lander
        fields = ('email', 'name',)
