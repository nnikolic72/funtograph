from django.shortcuts import render
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from .models import (
    Photographer,
    PhotoTeamManager,
    PhotoJudge,
    PhotoArtLover,
)

from photos.models import (
    Photo,
    PhotoToPhotographer
)

class CharactersIndexView(TemplateView):
    """
    View to show top Photographers and search form
    """
    template_name = 'characters/photographer_index.html'

    def get(self, request, *args, **kwargs):
        """
        Handle get request

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        if request.user.is_authenticated():
            photographers = Photographer.objects.all()
            return render(request,
                          self.template_name,
                          dict(
                              photographers=photographers,

                              )
            )
        else:
            return HttpResponseRedirect(reverse('members:register'))


class CharactersPhotographerIndexView(TemplateView):
    template_name = 'characters/photographer_details.html'

    def get(self, request, *args, **kwargs):
        """
        Handle get request

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        if request.user.is_authenticated():
            photographer_name = kwargs['p_photographer_name']

            try:
                photographer = Photographer.objects.get(name=photographer_name)
            except ObjectDoesNotExist:
                photographer = None


                #photo_to_photographer = PhotoToPhotographer(photographer=photographer, is_author=True)
            photographers_photos = Photo.objects.filter(owner=photographer)

            return render(request,
                          self.template_name,
                          dict(
                              photographer=photographer,
                              photographers_photos=photographers_photos,

                              )
            )
        else:
            return HttpResponseRedirect(reverse('members:register'))