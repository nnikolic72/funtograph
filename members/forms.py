from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from django.utils.translation import ugettext as _

from .models import Member

__author__ = 'n.nikolic'


class UserField(forms.CharField):
    """
    Helper class for username entry - clean method overriden
    """

    def clean(self, value):
        super(UserField, self).clean(value)
        try:
            User.objects.get(username=value)
            raise forms.ValidationError(_("Someone is already using this username. Please pick an other."))
        except User.DoesNotExist:
            return value


class UserForm(Form):
    """
    For registering as a new user and for editing existing user data
    """
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '8 characters minimum',
                                                                  }),
                                required=True,
                                )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '8 characters minimum',
                                                                  }),
                                required=True,
                                )

    username = UserField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': _('Your screen name in game'),
                                                       }),
                         required=True,
                         )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': _('Your real first name'),
                                                               }),
                                 required=False,
                                 )

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': _('Your real first name'),
                                                              }),
                                required=False,
                                )

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': _('Your valid email address'),
                                                            }),
                             required=True,
                             )


    def clean_password(self):
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError(_('Passwords are not the same'))
        if (self.data['password1'] == '') or (self.data['password2'] == ''):
            raise forms.ValidationError(_('You must fill both password fields'))

        return self.data['password1']

    def clean(self,*args, **kwargs):
        self.clean_password()
        return super(UserForm, self).clean(*args, **kwargs)


class LoginForm(Form):
    """
    Login form - for logging in to Funtograph
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': '8 characters minimum',
                                                                 }),
                               required=True,
                               )

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': _('Your screen name in game'),
                                                             }),
                               required=True,
                               )


class MemberForm(ModelForm):

    picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Your profile picture',
                                                             }
                                                      ),
                               required=False

    )
    class Meta:
        model = Member
        fields = ('picture',)