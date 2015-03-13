from django.contrib.auth.models import User
from django.db import models

import cloudinary

# Create your models here.
from django.utils.datetime_safe import datetime


class Member(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = cloudinary.models.CloudinaryField('image')

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username