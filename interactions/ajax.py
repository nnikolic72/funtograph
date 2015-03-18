__author__ = 'n.nikolic'

import json
from django.core.exceptions import ObjectDoesNotExist

from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form


from funtograph.settings.base import STATIC_URL
from members.models import Member
from characters.models import PhotoArtLover
from interactions.models import (
    Like,
    Favorite,
    Comment
)

from photos.models import Photo

from .forms import CommentForm

@dajaxice_register
def like(req, p_photo_id):
    """
    Like/unlike a photo in Funtograph

    :param req: HTTP request
    :type req:
    :param p_photo_id: Id of a photo to like
    :type p_photo_id: Integer
    :return:
    :rtype: Json
    """

    # First check if photo is liked by Member
    photo_instance = None
    like_action_result = 'error'
    no_of_likes = 0

    try:
        photo_instance = Photo.objects.get(id=p_photo_id)
    except ObjectDoesNotExist:
        photo_instance = None

    if photo_instance:
        logged_user_id = req.user.id
        if logged_user_id:
            try:
                # is logged user a member?
                logged_member = Member.objects.get(user__id=logged_user_id)
            except ObjectDoesNotExist:
                logged_member = None

            if logged_member:
                # Logged user is a member. Get their PhotoArtLover object
                logged_photo_art_lover = logged_member.get_my_photo_art_lover

                if logged_photo_art_lover:
                    # Logged member has a photo art lover character
                    #already_liked = False
                    like_instance = None
                    try:
                        like_instance = Like.objects.get(
                            members_likers=logged_photo_art_lover,
                            photo=photo_instance
                        )
                        already_liked = True
                    except ObjectDoesNotExist:
                        already_liked = False

                    if already_liked:
                        # we need to unlike the photo
                        if like_instance:
                            like_instance.delete()
                            like_action_result = 'unliked'
                    else:
                        # we need to like the photo
                        new_like = Like(
                            members_likers=logged_photo_art_lover,
                            photo=photo_instance
                        )
                        new_like.save()
                        like_action_result = 'liked'

            no_of_likes = Like.objects.filter(photo__id=p_photo_id).count()

    return json.dumps({'p_photo_id': p_photo_id,
                       'like_action_result': like_action_result,
                       #'static_url': STATIC_URL,
                       'no_of_likes': no_of_likes
    }
    )


@dajaxice_register
def favorite(req, p_photo_id):
    """
    Favorite/Unfavorite a photo in Funtograph

    :param req: HTTP request
    :type req:
    :param p_photo_id: Id of a photo to favorite
    :type p_photo_id: Integer
    :return:
    :rtype: Json
    """

    # First check if photo is liked by Member
    photo_instance = None
    favorite_action_result = 'error'
    no_of_favorites = 0

    try:
        photo_instance = Photo.objects.get(id=p_photo_id)
    except ObjectDoesNotExist:
        photo_instance = None

    if photo_instance:
        logged_user_id = req.user.id
        if logged_user_id:
            try:
                # is logged user a member?
                logged_member = Member.objects.get(user__id=logged_user_id)
            except ObjectDoesNotExist:
                logged_member = None

            if logged_member:
                # Logged user is a member. Get their PhotoArtLover object
                logged_photo_art_lover = logged_member.get_my_photo_art_lover

                if logged_photo_art_lover:
                    # Logged member has a photo art lover character

                    favorite_instance = None
                    try:
                        favorite_instance = Favorite.objects.get(
                            members_favoriters=logged_photo_art_lover,
                            photo=photo_instance
                        )
                        already_favorited = True
                    except ObjectDoesNotExist:
                        already_favorited = False

                    if already_favorited:
                        # we need to unlike the photo
                        if favorite_instance:
                            favorite_instance.delete()
                            favorite_action_result = 'unfavorited'
                    else:
                        # we need to like the photo
                        new_favorite = Favorite(
                            members_favoriters=logged_photo_art_lover,
                            photo=photo_instance
                        )
                        new_favorite.save()
                        favorite_action_result = 'favorited'

            no_of_favorites = Favorite.objects.filter(photo__id=p_photo_id).count()

    return json.dumps({'p_photo_id': p_photo_id,
                       'favorite_action_result': favorite_action_result,
                       #'static_url': STATIC_URL,
                       'no_of_favorites': no_of_favorites
    }
    )

@dajaxice_register
def send_comment(req, p_photo_id, form):
    """
    AJAX function to send comment to a photo
    :param req:
    :type req:
    :param form:
    :type form:
    :return:
    :rtype:
    """

    comment_form = CommentForm(form)

    if comment_form.is_valid():
        logged_user_id = req.user.id
        if logged_user_id:
            try:
                # is logged user a member?
                logged_member = Member.objects.get(user__id=logged_user_id)
            except ObjectDoesNotExist:
                logged_member = None

            if logged_member:
                # Logged user is a member. Get their PhotoArtLover object
                logged_photo_art_lover = logged_member.get_my_photo_art_lover

                if logged_photo_art_lover:

                    #Create a comment
                    try:
                        commented_photo = Photo.objects.get(id=p_photo_id)
                        #photo_art_= PhotoArtLover.objects.get(id=p_photo_art_lover_id)
                        cleaned_comment = comment_form.cleaned_data[u'comment_text']
                        new_comment = Comment(photo=commented_photo,
                                              comment_text=cleaned_comment,
                                              members_commenters=logged_photo_art_lover
                                              )
                        new_comment.save()
                    except ObjectDoesNotExist:
                        commented_photo = None



    return json.dumps({
        'comment_text': form.comment_text
    }
    )