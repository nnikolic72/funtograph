from datetime import timedelta, time
from django.utils.datetime_safe import datetime

__author__ = 'n.nikolic'
import json

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _

from dajaxice.decorators import dajaxice_register

from members.models import Member
from photos.models import Photo
from .models import PhotoDuel

@dajaxice_register
def photo_duel_vote(req, p_photo_duel_id, p_vote):
    """
    AJAX function to save photo duel vote
    :param req:
    :type req:
    :param p_photo_duel_id:
    :type p_photo_duel_id:
    :param p_vote:
    :type p_vote:
    :return: JSON for callback function
    :rtype:
    """

    action_result = 0

    try:
        photo_duel_instance = PhotoDuel.objects.get(id=p_photo_duel_id)
    except ObjectDoesNotExist:
        photo_duel_instance = None

    if photo_duel_instance:
        if req.user.is_authenticated():
            logged_user_id = req.user.id
            if logged_user_id:
                try:
                    # is logged user a member?
                    logged_member = Member.objects.get(user__id=logged_user_id)
                except ObjectDoesNotExist:
                    logged_member = None

                if logged_member:
                    # Logged user is a member. Get their Photographer object
                    logged_photographer = logged_member.get_my_photographer

                    if logged_photographer:
                        # Logged member has a photographer
                        if photo_duel_instance.active and photo_duel_instance.have_both_agreed:
                            if p_vote == 'a':
                                photo_duel_instance.votes_a.add(logged_photographer)
                            if p_vote == 'b':
                                photo_duel_instance.votes_b.add(logged_photographer)
                            if p_vote == 'x':
                                photo_duel_instance.undecided.add(logged_photographer)

                            #photo_duel_instance.save()
                            action_result = 1

                            photo_duels_left = PhotoDuel.objects.filter(active=True) \
                                .exclude(photo_a__owner=logged_photographer) \
                                .exclude(photo_b__owner=logged_photographer) \
                                .exclude(votes_a=logged_photographer) \
                                .exclude(votes_b=logged_photographer) \
                                .exclude(undecided=logged_photographer) \
                                .exclude(agreed_a=False) \
                                .exclude(agreed_b=False).count()

    return json.dumps({'p_photo_duel_id': p_photo_duel_id,
                       'p_vote': p_vote,
                       'action_result': action_result,
                       'photo_duels_left': photo_duels_left,
                       }
    )

@dajaxice_register
def photo_duel_challenge_complete(req, challenged_photo_id, my_photo_id):
    """
    Challenge photo challenged_photo_id to a duel against my_photo_id
    :param req:
    :type req:
    :param challenged_photo_id:
    :type challenged_photo_id:
    :param my_photo_id:
    :type my_photo_id:
    :return:
    :rtype:
    """
    action_result = 0
    l_duel_end_time = None
    challenged_photo_url = None
    my_photo_url = None

    if req.user.is_authenticated():
        logged_user_id = req.user.id
        if logged_user_id:
            try:
                # is logged user a member?
                logged_member = Member.objects.get(user__id=logged_user_id)
                logged_photographer = logged_member.get_my_photographer
            except ObjectDoesNotExist:
                logged_member = None
                logged_photographer = None

        if logged_member and logged_photographer:
            try:
                challenged_photo = Photo.objects.get(id=challenged_photo_id)
                challenged_photo_url = challenged_photo.get_big_thumbnail_url
            except ObjectDoesNotExist:
                challenged_photo = None

            try:
                my_photo = Photo.objects.get(id=my_photo_id)
                my_photo_url = my_photo.get_big_thumbnail_url
            except ObjectDoesNotExist:
                my_photo = None

            # Todo: agreed must be False
            challenged_photo_owner = challenged_photo_id
            l_duel_end_time = datetime.today() + timedelta(days=1, hours=2)
            l_duel_end_time_str = \
                "%04d-%02d-%02d %02d:%02d:%02d" % \
                (l_duel_end_time.year,
                 l_duel_end_time.month,
                 l_duel_end_time.day,
                 l_duel_end_time.hour,
                 l_duel_end_time.minute,
                 l_duel_end_time.second
                )
            new_duel = PhotoDuel(photo_a=challenged_photo,
                                 photo_b=my_photo,
                                 agreed_a=True,
                                 agreed_b=True,
                                 duel_start_time=datetime.today(),
                                 duel_end_time=l_duel_end_time,
                                 active=True
                                 )
            new_duel.save()
            action_result = 1

    return json.dumps({'challenged_photo_id': challenged_photo_id,
                       'my_photo_id': my_photo_id,
                       'action_result': action_result,
                       'duel_end_time': l_duel_end_time_str,
                       'left_photo_url': challenged_photo_url,
                       'right_photo_url': my_photo_url,
                       }
    )