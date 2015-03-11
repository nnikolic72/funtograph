from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class Lander(models.Model):
    """
    Extends Django model class
    """

    email = models.EmailField(null=True, blank=True)
    name = models.EmailField(null=True, blank=True)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        return super(Lander, self).save(*args, **kwargs)