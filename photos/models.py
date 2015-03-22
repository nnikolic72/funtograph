from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from cloudinary.models import CloudinaryField

from characters.models import (
                               Photographer)

from interactions.models import (
    Like,
    Comment,
    Favorite
)
# Create your models here.
from members.models import Member


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

    @property
    def get_thumbnail_url(self):
        """

        :return: Url of thumbnail image
        :rtype: String
        """
        photo_thumb_url = self.photo.build_url(transformation='media_lib_thumb')
        return photo_thumb_url

    @property
    def get_src_url(self):
        """

        :return: Url of thumbnail image
        :rtype: String
        """
        photo_src_url = self.photo.build_url()
        return photo_src_url

    @property
    def get_number_of_likes(self):
        """

        :return: Number of likes on a photo
        :rtype: Integer
        """

        likes_count = Like.objects.filter(photo=self, like_value=True).count()

        return likes_count

    @property
    def get_number_of_dislikes(self):
        """

        :return: Number of likes on a photo
        :rtype: Integer
        """

        # likes_count = Like.objects.filter(photo=self, like_value=True).count()
        dislikes_count = Like.objects.filter(photo=self, like_value=False).count()

        return dislikes_count

    @property
    def get_number_of_comments(self):
        """

        :return: Number of likes on a photo
        :rtype: Integer
        """

        comments_count = Comment.objects.filter(photo=self).count()
        return comments_count

    @property
    def get_comments(self):
        """

        :return: Number of likes on a photo
        :rtype: Comments object
        """

        photo_comments = Comment.objects.filter(photo=self)
        return photo_comments

    @property
    def get_last_four_comments(self ):
        """

        :return: Number of likes on a photo
        :rtype: Comments object
        """

        photo_comments = Comment.objects.filter(photo=self)
        photo_comments_len = len(photo_comments)
        if photo_comments_len > 4:
            photo_comments = photo_comments[photo_comments_len-4:photo_comments_len]
        return photo_comments

    @property
    def get_number_of_favorites(self):
        """

        :return: Number of likes on a photo
        :rtype: Integer
        """

        favorites_count = Favorite.objects.filter(photo=self).count()
        return favorites_count

    title = models.CharField(max_length=100,
                             verbose_name=_('Photo title'))
    owner = models.ManyToManyField(Photographer, null=True, blank=True)

    author = models.ForeignKey(Member, null=True, blank=True)

    photo = CloudinaryField('image', null=False)

    photo_wear = models.IntegerField(null=False, blank=False,
                                     default=0,
                                     verbose_name=_('Photo wear')
    )

    photo_price = models.IntegerField(null=False, blank=False,
                                      default=0,
                                      verbose_name=_('Photo price')
    )

    avg_photo_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0,
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

    phash = models.CharField(max_length=200, null=True, blank=True)
    format = models.CharField(max_length=20, null=True, blank=True)
    dominant_color = models.CharField(max_length=20, null=True, blank=True)
    full_url = models.URLField(null=True, blank=True)
    photo_creation_date = models.CharField(max_length=20, null=True, blank=True)
    creator_tool = models.CharField(max_length=200, null=True, blank=True)
    lens_model = models.CharField(max_length=100, null=True, blank=True)
    camera_make = models.CharField(max_length=100, null=True, blank=True)
    camera_model = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    # loot = many to many field to Loot class, with through class LootAmount

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

