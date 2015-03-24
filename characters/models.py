from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from funtograph.settings.base import MAX_UPLOAD_PHOTOS_DEFAULT
import cloudinary
# Create your models here.


class Photographer(models.Model):
    def is_character_active(self):
        return self.character_active

    member = models.ForeignKey('members.Member', null=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    level = models.IntegerField(default=1, blank=False, null=False)
    current_xp = models.IntegerField(default=0, blank=False, null=False)
    total_xp = models.IntegerField(default=0, blank=False, null=False)

    character_active = models.BooleanField(default=True, blank=False, null=False)

    max_photos_to_upload = models.IntegerField(default=MAX_UPLOAD_PHOTOS_DEFAULT,
                                               null=False, blank=False)

    photo_wear_limit = models.IntegerField(default=5, blank=False, null=False)

    allowed_to_duel = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_team_duel = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_join_league = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_found_collective = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_like = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_comment = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_favorite = models.BooleanField(default=True, blank=False, null=False)
    allowed_to_see_stats = models.BooleanField(default=False, blank=False, null=False)


    last_vote_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()



    #loot = many to many field to Loot class, with through class LootAmount

    def __unicode__(self):
        """

        :return: Name of the character
        :rtype: String
        """
        return self.name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Photographer, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = _('created_at')
        ordering = (_('-level'), _('-current_xp'), _('name'),)


