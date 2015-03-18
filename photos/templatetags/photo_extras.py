__author__ = 'n.nikolic'

from django import template

register = template.Library()


from interactions.models import Like

@register.simple_tag
def has_photographer_liked(photo_art_lover, photo):
    """

    :param photographer: PhotoArtLover
    :type photographer:
    :param photo: Photo
    :type photo:
    :return: True/False
    :rtype:
    """
    has_liked = False

    no_of_likes = Like.objects.filter(
        members_likers=photo_art_lover,
        photo=photo
    ).count()

    if no_of_likes > 0:
        has_liked = True

    return has_liked

