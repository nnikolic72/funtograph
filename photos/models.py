from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from  cloudinary.models import CloudinaryField

from characters.models import (Character,
                               Photographer)


# Create your models here.

class PhotoCategory(models.Model):
    """
    Categories that can be assigned to a photo
    """

    def __unicode__(self):
        '''return text for this class'''
        return self.name

    name = models.CharField(max_length=200, null=False, blank=False, default='',
                            verbose_name=_('Photo category name')
    )
    description = models.CharField(max_length=200, null=True, blank=True, default='',
                                   verbose_name=_('Photo category description')
    )
    slug = models.SlugField(max_length=50, null=True, blank=True, default='',
                            verbose_name=_('Photo category slug')
    )

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(PhotoCategory, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Photo Category')
        verbose_name_plural = _('Photo Categories')


class PhotoAttribute(models.Model):
    """Provide attributes that can be assigned to a photo"""

    def __unicode__(self):
        """return text for this class"""
        return self.name

    name = models.CharField(max_length=50, null=False, blank=False, default='',
                            verbose_name=_('Photo attribute name')
    )
    description = models.CharField(max_length=200, null=True, blank=True, default='',
                                   verbose_name=_('Photo attribute description')
    )
    slug = models.SlugField(max_length=50, null=True, blank=True, default='',
                            verbose_name=_('Photo attribute slug')
    )

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(PhotoAttribute, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name', )
        verbose_name = _('Photo Attribute')
        verbose_name_plural = _('Photo Attributes')


class Photo(models.Model):
    """
    Model for storing members photos, and their metadata
    """
    title = models.CharField(max_length=100,
                             verbose_name=_('Photo title'))
    owner = models.ManyToManyField(Photographer, through='PhotoToPhotographer',
                                    through_fields=('photo', 'photographer')
    )

    photo = CloudinaryField('image', null=False)

    photo_wear = models.IntegerField(null=False, blank=False,
                                      default=0,
                                      verbose_name=_('Photo wear')
    )

    photo_price = models.IntegerField(null=False, blank=False,
                                      default=0,
                                      verbose_name=_('Photo price')
    )

    avg_photo_rating = models.DecimalField(max_digits=3,decimal_places=2, default=0,
                                           null=True, blank=True,
                                           verbose_name=_('Average photo rating')
    )

    categories = models.ManyToManyField(PhotoCategory, null=True, blank=True,
                                        verbose_name=_('Photo Categories')
    )
    attributes = models.ManyToManyField(PhotoAttribute, null=True, blank=True,
                                        verbose_name=_('Photo Attributes')
    )

    for_sale = models.BooleanField(null=False, blank=False, default=False,
                                   verbose_name=_('Photo is for sale')
    )
    active = models.BooleanField(null=False, blank=False, default=True,
                                 verbose_name=_('Photo is active')
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
        return super(Photo, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')


class PhotoToPhotographer(models.Model):

    photo = models.ForeignKey(Photo)
    photographer = models.ForeignKey(Photographer)

    is_author = models.BooleanField(default=True, null=False, blank=False)
    is_manager = models.BooleanField(default=False, null=False, blank=False)
