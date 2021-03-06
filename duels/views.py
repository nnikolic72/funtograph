from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from members.models import Member

from funtograph.settings.base import (
    INITIAL_PHOTO_DUELS_TO_DISPLAY
)

from photos.models import Photo
from .models import PhotoDuel

# Create your views here.
class PhotoDuelsView(TemplateView):
    """
    Shows main Duel dashboard
    """

    template_name = 'duels/index.html'

    def get(self, request, *args, **kwargs):
        """
        Get request reply

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        photographer = None
        if request.user.is_authenticated():
            try:
                logged_member = Member.objects.get(user__id=request.user.id)
                photographer = logged_member.get_my_photographer
            except ObjectDoesNotExist:
                logged_member = None

            photo_duels = PhotoDuel.objects.filter(active=True) \
                .exclude(photo_a__owner=photographer) \
                .exclude(photo_b__owner=photographer) \
                .exclude(votes_a=photographer) \
                .exclude(votes_b=photographer) \
                .exclude(undecided=photographer) \
                .exclude(agreed_a=False) \
                .exclude(agreed_b=False)

            if len(photo_duels) > INITIAL_PHOTO_DUELS_TO_DISPLAY:
                photo_duels = photo_duels[0:INITIAL_PHOTO_DUELS_TO_DISPLAY]

            #available_photo_duels = []
            #for photo_duel in photo_duels:
            #    if photo_duel.can_photographer_vote(photographer):
            #        available_photo_duels.append([photo_duel])
            #        #photo_duels.exclude(id=photo_duel.id)

            return render(request,
                          self.template_name,
                          dict(
                              photo_duels=photo_duels,

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



class PhotoDuelsChallengeView(TemplateView):
    """
    Template for duel challenge - lists all logged users photos
    """
    template_name = 'duels/challenge.html'

    def get(self, request, *args, **kwargs):
        """
        Get request reply

        :param request:
        :type request:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """

        photographer = None
        challenged_photo_id = kwargs['p_photo_id']

        if request.user.is_authenticated():
            try:
                logged_member = Member.objects.get(user__id=request.user.id)
                photographer = logged_member.get_my_photographer
            except ObjectDoesNotExist:
                logged_member = None

            if logged_member and photographer:
                own_photos = Photo.objects.filter(
                    owner=photographer,
                    active=True,
                    photo_wear__lt=photographer.photo_wear_limit + 1

                )
                try:
                    challenged_photo = Photo.objects.get(id=challenged_photo_id)
                except ObjectDoesNotExist:
                    challenged_photo = None

            return render(request,
                          self.template_name,
                          dict(
                              own_photos=own_photos,
                              own_photos_count=own_photos.count(),
                              challenged_photo=challenged_photo,

                              statusbar_level=photographer.level,
                              statusbar_name=photographer.name,
                              statusbar_current_xp=photographer.current_xp,
                              statusbar_funtocredits=logged_member.funtocredits,
                              statusbar_current_energy=logged_member.current_energy,
                              statusbar_max_energy=logged_member.max_energy,
                              )
            )

