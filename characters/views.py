from django.shortcuts import render
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from .models import (
    Photographer
)

from photos.models import (
    Photo,
)

from interactions.models import (
    Like,
    Favorite,
    Comment
)

from interactions.forms import CommentForm

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
            photographer_interactions = None
            photographers_photos = None
            photographer = None
            user_is_gallery_owner = False
            photographers_photos = []

            try:
                photographer = Photographer.objects.get(name=photographer_name)
            except ObjectDoesNotExist:
                photographer = None

            try:
                my_photo_art_lover = Photographer.objects.get(name=photographer_name)
            except ObjectDoesNotExist:
                my_photo_art_lover = None


                #photo_to_photographer = PhotoToPhotographer(photographer=photographer, is_author=True)
            if photographer:
                if photographer.member.user.id == request.user.id:
                    user_is_gallery_owner = True
                photographers_photos = Photo.objects.filter(owner=photographer)
                liked_photos_set = \
                    Like.objects.filter(
                        members_likers=photographer,
                        photo__in=photographers_photos,
                        like_value=True
                    ).select_related('photo')

                unliked_photos_set = \
                    Like.objects.filter(
                        members_likers=photographer,
                        photo__in=photographers_photos,
                        like_value=False
                    ).select_related('photo')

                favorited_photos_set = \
                    Favorite.objects.filter(
                        members_favoriters=photographer,
                        photo__in=photographers_photos
                    ).select_related('photo')

                liked_photos = []
                for p in liked_photos_set:
                    liked_photos.extend([p.photo])

                unliked_photos = []
                for p in unliked_photos_set:
                    unliked_photos.extend([p.photo])

                favorited_photos = []
                for p in favorited_photos_set:
                    favorited_photos.extend([p.photo])

            return render(request,
                          self.template_name,
                          dict(
                              photographer=photographer,
                              photographers_photos=photographers_photos,
                              liked_photos=liked_photos,
                              unliked_photos=unliked_photos,
                              favorited_photos=favorited_photos,
                              comment_form=CommentForm,
                              user_is_gallery_owner=user_is_gallery_owner,
                              my_photo_art_lover=my_photo_art_lover,
                          )
            )
        else:
            return HttpResponseRedirect(reverse('members:register'))