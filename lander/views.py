from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext as _

# Create your views here.
from django.views.generic.base import TemplateView

from .forms import SignUpForm
from funtograph.settings.base import SHOW_TRANSLATIONS

class LanderHomePageView(TemplateView):
    ''' Home page of lander app
    '''

    template_name = 'lander/index.html'

    def get(self, request, *args, **kwargs):
        '''Serve GET request'''

        return render(request, self.template_name,
                      dict(request=request, form=SignUpForm(),
                           SHOW_TRANSLATIONS=SHOW_TRANSLATIONS,)
        )

class LanderSignUpView(TemplateView):
    ''' Thank you page
    '''

    template_name = 'lander/signup.html'

    def get(self, request, *args, **kwargs):
        '''Serve GET request'''

        return render(request, self.template_name,
                      dict(request=request, ))
