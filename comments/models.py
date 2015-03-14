from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from photos.models import Photo
from characters.models import Character
# Create your models here.


class Comment(models.Model):
    """
    Comments left on the photos by characters
    """

    photo = models.ForeignKey(Photo)
    comment_source_character = models.ForeignKey(Character)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Comment, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.comment_source_character

    class Meta:
        ordering = [_('created_at')]
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')