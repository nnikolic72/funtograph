__author__ = 'n.nikolic'

import json
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _

from dajaxice.decorators import dajaxice_register
#from dajaxice.utils import deserialize_form


from funtograph.settings.base import STATIC_URL
from members.models import Member
from characters.models import Photographer
from interactions.models import (
    Like,
    Favorite,
    Comment
)

from photos.models import Photo

from .forms import CommentForm

@dajaxice_register
def like(req, p_photo_id, p_pressed_button):
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
                # Logged user is a member. Get their Photographer object
                logged_photographer = logged_member.get_my_photographer

                if logged_photographer:
                    # Logged member has a photo art lover character
                    #already_liked = False
                    like_instance = None

                    try:
                        like_instance = Like.objects.get(
                            members_likers=logged_photographer,
                            photo=photo_instance,
                            )
                        make_new_like = False
                    except ObjectDoesNotExist:
                        make_new_like = True

                    if make_new_like:
                        if p_pressed_button == 'like_button':
                            l_like_value = True
                        else:
                            #Then it's unlike button
                            l_like_value = False

                        new_like = Like(
                            members_likers=logged_photographer,
                            photo=photo_instance,
                            like_value=l_like_value
                        )
                        new_like.save()
                        like_action_result = p_pressed_button + '-pressed'
                    else:
                        # we need to change existing like
                        delete_existing_like = False
                        if p_pressed_button == 'like_button':
                            if like_instance.like_value:
                                delete_existing_like = True

                        else:
                            # then it's unlike button
                            if not like_instance.like_value:
                                delete_existing_like = True

                        if delete_existing_like:
                            like_instance.delete()
                            like_action_result = p_pressed_button + '-unpressed'
                        else:
                            like_instance.like_value = not like_instance.like_value
                            like_instance.save()
                            like_action_result = p_pressed_button + '-pressed'

        no_of_likes = photo_instance.get_number_of_likes
        no_of_dislikes = photo_instance.get_number_of_dislikes

        return json.dumps({'p_photo_id': p_photo_id,
                           'like_action_result': like_action_result,
                           'no_of_likes': no_of_likes,
                           'no_of_dislikes': no_of_dislikes
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
                # Logged user is a member. Get their Photographer object
                logged_photographer = logged_member.get_my_photographer

                if logged_photographer:
                    # Logged member has a photo art lover character

                    favorite_instance = None
                    try:
                        favorite_instance = Favorite.objects.get(
                            members_favoriters=logged_photographer,
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
                            members_favoriters=logged_photographer,
                            photo=photo_instance
                        )
                        new_favorite.save()
                        favorite_action_result = 'favorited'

            no_of_favorites = Favorite.objects.filter(photo__id=p_photo_id).count()

    return json.dumps({'p_photo_id': p_photo_id,
                       'favorite_action_result': favorite_action_result,
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
    comment_added = False
    commented_photo = Photo.objects.get(id=p_photo_id)
    comments_text = _('Comments:')

    if comment_form.is_valid():
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

                    #Create a comment
                    try:
                        cleaned_comment = comment_form.cleaned_data[u'comment_text']
                        if (cleaned_comment != '') and (cleaned_comment is not None):

                            #photo_art_= Photographer.objects.get(id=p_photo_art_lover_id)

                            new_comment = Comment(photo=commented_photo,
                                                  comment_text=cleaned_comment,
                                                  members_commenters=logged_photographer
                            )
                            new_comment.save()
                            comment_added = True
                    except ObjectDoesNotExist:
                        cleaned_comment = None
                        logged_photographer = None
                        commented_photo = None

    no_of_comments = commented_photo.get_number_of_comments
    if no_of_comments == 1:
        p_is_first = 1
    else:
        p_is_first = 0

    return json.dumps({
        'comment_text': cleaned_comment,
        'logged_photographer_name': logged_photographer.name,
        'p_photo_id': commented_photo.id,
        'no_of_comments': no_of_comments,
        'p_is_first': p_is_first,
        'new_comment_id': new_comment.id,
        'comments_text': comments_text,
        }
    )


@dajaxice_register
def delete_comment(req, p_comment_id):
    """
    AJAX function to delete comment from photo

    :param req:
    :type req:
    :param p_photo_id:
    :type p_photo_id:
    :param form:
    :type form:
    :return:
    :rtype:
    """

    action_result = 'error'
    no_of_comments = 0
    no_more_comments_translation = None

    try:
        comment_instance = Comment.objects.get(id=p_comment_id)
        photo = comment_instance.photo
    except ObjectDoesNotExist:
        comment_instance = None
        photo = None

    if comment_instance:
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
                    comment_instance.delete()
                    action_result = 'deleted'

            no_of_comments = Comment.objects.filter(photo=photo).count()
            no_more_comments_translation = _('No comments on this photo. Be the first one to comment!')

    return json.dumps({'p_comment_id': p_comment_id,
                       'action_result': action_result,
                       'no_of_comments': no_of_comments,
                       'p_photo_id': photo.id,
                       'no_more_comments_translation': no_more_comments_translation,
    }
    )


@dajaxice_register
def like_comment(req, p_comment_id):
    """
    AJAX function to delete comment from photo

    :param req:
    :type req:
    :param p_photo_id:
    :type p_photo_id:
    :param form:
    :type form:
    :return:
    :rtype:
    """

    action_result = 'error'
    #no_of_comments = 0
    no_of_not_liked_comments = 0

    try:
        comment_instance = Comment.objects.get(id=p_comment_id)
        photo = comment_instance.photo
    except ObjectDoesNotExist:
        comment_instance = None
        photo = None

    if comment_instance:
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
                    l_liked_by_author = not comment_instance.liked_by_author
                    comment_instance.liked_by_author = l_liked_by_author
                    comment_instance.save()
                    if l_liked_by_author:
                        action_result = 'liked'
                    else:
                        action_result = 'unliked'

            no_of_not_liked_comments = \
                Comment.objects.filter(photo=photo,liked_by_author=False).\
                    exclude(members_commenters=logged_photographer).count()

    return json.dumps({'p_comment_id': p_comment_id,
                       'action_result': action_result,
                       'no_of_not_liked_comments': no_of_not_liked_comments
    }
    )