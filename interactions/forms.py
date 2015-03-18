__author__ = 'n.nikolic'

from django import forms
from django.forms import ModelForm, Form
from django.utils.translation import ugettext as _

from .models import Comment

class CommentForm(Form):
    """
    Form for commenting on a photo
    """

    comment_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': unicode(Comment._meta.get_field('comment_text').help_text)}
                                                          ),
                                   required=False,
                                   )