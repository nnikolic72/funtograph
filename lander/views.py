from django.shortcuts import render
from django.utils.translation import ugettext as _

# Create your views here.
from django.views.generic.base import TemplateView


class LanderHomePageView(TemplateView):
    ''' Home page of lander app
    '''

    template_name = 'lander/index.html'
    # Translators: header of landing page


    # Translators: Keep &raquo; text intact.

    def get(self, request, *args, **kwargs):
        '''Serve GET request'''

        return render(request, self.template_name, {
        }
        )