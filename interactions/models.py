from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime



# Create your models here.
class Like(models.Model):
    """
    Likes data models
    """
    photo = models.ForeignKey('photos.Photo')
    members_likers = models.ForeignKey('characters.PhotoArtLover')

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Like, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')


class Comment(models.Model):
    """
    Comments data models
    """
    photo = models.ForeignKey('photos.Photo')
    members_commenters = models.ForeignKey('characters.PhotoArtLover')
    comment_text = models.CharField(max_length=300, blank=True, null=True,
                                    help_text=_('Comment up to 300 characters. Be polite!')
    )

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Comment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class Favorite(models.Model):
    """
    Comments data models
    """
    photo = models.ForeignKey('photos.Photo')
    members_favoriters = models.ForeignKey('characters.PhotoArtLover')

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Favorite, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')
