from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from photos.models import Photo
from members.models import Member


# Create your models here.
class Like(models.Model):
    """
    Likes data models
    """
    photo = models.ForeignKey(Photo)
    members_likers = models.ForeignKey(Member)
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
    photo = models.ForeignKey(Photo)
    members_likers = models.ForeignKey(Member)
    comment_text = models.CharField(max_length=300, blank=True, null=True)

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