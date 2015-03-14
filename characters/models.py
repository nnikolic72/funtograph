from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

import cloudinary
# Create your models here.


class Character(models.Model):
    def is_character_active(self):
        return self.character_active

    name = models.CharField(max_length=50, blank=False, null=False)
    level = models.IntegerField(default=1, blank=False, null=False)
    current_xp = models.IntegerField(default=0, blank=False, null=False)
    total_xp = models.IntegerField(default=0, blank=False, null=False)

    character_active = models.BooleanField(default=True, blank=False, null=False)

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
        abstract = True
        get_latest_by = _('created_at')
        ordering = (_('name'),)


class PhotoArtLover(Character):
    """
    Role: PhotoArtLover
    """

    character_type = _('Photo Art Lover')

    class Meta(Character):
        verbose_name = _('Photo Art Lover')
        verbose_name_plural = _('Photo Art Lovers')



class PhotoJudge(Character):
    """
    Role: PhotoArtLover
    """

    character_type = _('Photo Judge')

    class Meta(Character):
        verbose_name = _('Photo Judge')
        verbose_name_plural = _('Photo Judges')



class PhotoTeamManager(Character):
    """
    Role: PhotoArtLover
    """

    character_type = _('Photo Team Manager')

    class Meta(Character):
        verbose_name = _('Photo Team Manager')
        verbose_name_plural = _('Photo Team Managers')


class Photographer(Character):
    """
    Role: PhotoArtLover
    """

    character_type = _('Photographer')

    class Meta(Character):
        verbose_name = _('Photographer')
        verbose_name_plural = _('Photographers')

