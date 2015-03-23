from django.shortcuts import render
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _

# Create your views here.
from members.models import Member

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

from duels.models import (
    PhotoDuel
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
            try:
                logged_member = Member.objects.get(user__id=request.user.id)
                photographer = logged_member.get_my_photographer
            except ObjectDoesNotExist:
                logged_member = None

            photographers = Photographer.objects.all()
            return render(request,
                          self.template_name,
                          dict(
                              photographers=photographers,

                              statusbar_level=photographer.level,
                              statusbar_name=photographer.name,
                              statusbar_current_xp=photographer.current_xp,
                              statusbar_funtocredits=logged_member.funtocredits,
                              statusbar_current_energy=logged_member.current_energy,
                              statusbar_max_energy=logged_member.max_energy,
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

        liked_photos = None
        unliked_photos = None
        favorited_photos = None
        challenged_photos = None

        if request.user.is_authenticated():

            photographer_name = kwargs['p_photographer_name']
            photographer_interactions = None
            photographers_photos = None
            photographer = None
            user_is_gallery_owner = False
            photographers_photos = []

            try:
                logged_member = Member.objects.get(user__id=request.user.id)
            except ObjectDoesNotExist:
                logged_member = None

            try:
                photographer = Photographer.objects.get(name=photographer_name)
            except ObjectDoesNotExist:
                photographer = None

            try:
                my_photographer = Photographer.objects.get(member=logged_member)
            except ObjectDoesNotExist:
                my_photographer = None

            if photographer and logged_member and my_photographer:
                if photographer.member.user.id == request.user.id:
                    user_is_gallery_owner = True
                photographers_photos = Photo.objects.filter(owner=photographer)
                liked_photos_set = \
                    Like.objects.filter(
                        members_likers=my_photographer,
                        photo__in=photographers_photos,
                        like_value=True
                    ).select_related('photo')

                unliked_photos_set = \
                    Like.objects.filter(
                        members_likers=my_photographer,
                        photo__in=photographers_photos,
                        like_value=False
                    ).select_related('photo')

                favorited_photos_set = \
                    Favorite.objects.filter(
                        members_favoriters=my_photographer,
                        photo__in=photographers_photos
                    ).select_related('photo')

                challenged_a_photos_set = \
                    PhotoDuel.objects.filter(
                        active=True,
                        photo_a__owner=my_photographer,
                        photo_b__owner=photographer,

                    ).select_related('photo_b')

                challenged_a_photos_set_agreed = \
                    PhotoDuel.objects.filter(
                        active=True,
                        photo_a__owner=my_photographer,
                        photo_b__owner=photographer,
                        agreed_b=True
                    ).select_related('photo_b')

                challenged_b_photos_set = \
                    PhotoDuel.objects.filter(
                        active=True,
                        photo_a__owner=photographer,
                        photo_b__owner=my_photographer
                    ).select_related('photo_a')

                challenged_b_photos_set_agreed = \
                    PhotoDuel.objects.filter(
                        active=True,
                        photo_a__owner=photographer,
                        photo_b__owner=my_photographer,
                        agreed_a=True
                    ).select_related('photo_a')

                liked_photos = []
                for p in liked_photos_set:
                    liked_photos.extend([p.photo])

                unliked_photos = []
                for p in unliked_photos_set:
                    unliked_photos.extend([p.photo])

                favorited_photos = []
                for p in favorited_photos_set:
                    favorited_photos.extend([p.photo])

                challenged_photos = []
                for p in challenged_a_photos_set:
                    challenged_photos.extend([p.photo_b])
                for p in challenged_b_photos_set:
                    challenged_photos.extend([p.photo_a])

                challenged_photos_agreed = []
                for p in challenged_a_photos_set_agreed:
                    challenged_photos_agreed.extend([p.photo_b])
                for p in challenged_b_photos_set_agreed:
                    challenged_photos_agreed.extend([p.photo_a])

            return render(request,
                          self.template_name,
                          dict(
                              photographer=photographer,
                              photographers_photos=photographers_photos,
                              liked_photos=liked_photos,
                              unliked_photos=unliked_photos,
                              favorited_photos=favorited_photos,
                              challenged_photos=challenged_photos,
                              comment_form=CommentForm,
                              user_is_gallery_owner=user_is_gallery_owner,
                              my_photographer=my_photographer,

                              statusbar_level=photographer.level,
                              statusbar_name=photographer.name,
                              statusbar_current_xp=photographer.current_xp,
                              statusbar_funtocredits=logged_member.funtocredits,
                              statusbar_current_energy=logged_member.current_energy,
                              statusbar_max_energy=logged_member.max_energy,
                              )
            )
        else:
            return HttpResponseRedirect(reverse('members:register'))