from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from  cloudinary.models import CloudinaryField

from characters.models import (Character,
                               Photographer)


# Create your models here.





class Photo(models.Model):
    """
    Model for storing members photos, and their metadata
    """
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Photographer, through='PhotoToPhotographer',
                                    through_fields=('photo', 'photographer')
    )

    photo = CloudinaryField('image')

    avg_photo_rating = models.DecimalField(max_digits=3,decimal_places=2, default=0,
                                           null=True, blank=True
    )



    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    #loot = many to many field to Loot class, with through class LootAmount

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Character, self).save(*args, **kwargs)

    class Meta:
        ordering = ['user__username']
        verbose_name = _('Member')
        verbose_name_plural = _('Members')


class PhotoToPhotographer(models.Model):

    photo = models.ForeignKey(Photo)
    photographer = models.ForeignKey(Photographer)

    is_author = models.BooleanField(default=True, null=False, blank=False)
    is_manager = models.BooleanField(default=False, null=False, blank=False)
