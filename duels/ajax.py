__author__ = 'n.nikolic'
import json

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _

from dajaxice.decorators import dajaxice_register

from members.models import Member
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
