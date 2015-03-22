from django import forms
from django.forms import ModelForm, Form
from django.utils.translation import ugettext as _
import cloudinary

from .models import (Photo, PhotoCategory, PhotoAttribute)

__author__ = 'n.nikolic'

class PhotoUploadForm(Form):
    """
    Class to define form for uploading photos
    """

    photo = cloudinary.forms.CloudinaryFileField(required=True,
                                                 options = {
                                                     'tags': 'member_upload',
                                                     'crop': 'pad',
                                                     'width': 600,
                                                     'height': 600,
                                                     'image_metadata': True,
                                                     'phash': True,
                                                     'colors': True,
                                                 }
    )

    csrfmiddlewaretoken = forms.HiddenInput()

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': unicode(Photo._meta.get_field('title').help_text)}
                                                   ),
                            required=True,
                            )

    categories = forms.ModelMultipleChoiceField(queryset=PhotoCategory.objects.all(), required=True)
    attributes = forms.ModelMultipleChoiceField(queryset=PhotoAttribute.objects.all(), required=True)