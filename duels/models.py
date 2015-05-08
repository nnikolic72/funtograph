from django.db import models
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime

from cloudinary.models import CloudinaryField

#from photos.models import Photo
from characters.models import Photographer


# Create your models here.
class PhotoDuel(models.Model):
    """
    Class model for basic photo duel
    """

    photo_a = models.ForeignKey('photos.Photo', null=True, blank=True,
                                verbose_name=_('Photo A'),
                                related_name='photo_a')
    photo_b = models.ForeignKey('photos.Photo',  null=True, blank=True,
                                verbose_name=_('Photo B'),
                                related_name='photo_b')

    agreed_a = models.NullBooleanField(default=False,  null=True, blank=True,
                                       verbose_name=_('Photographer A has agreed to duel'))
    agreed_b = models.NullBooleanField(default=False,  null=True, blank=True,
                                       verbose_name=_('Photographer B has agreed to duel'))

    votes_a = models.ManyToManyField(Photographer, null=True, blank=True, related_name='votes_a')
    votes_b = models.ManyToManyField(Photographer,  null=True, blank=True, related_name='votes_b')

    undecided = models.ManyToManyField(Photographer,  null=True, blank=True, related_name='votes_undecided')

    winner = models.CharField(max_length=1, null=True, blank=True)

    duel_start_time = models.DateTimeField(verbose_name=_('Duel start time'), null=True, blank=True)
    duel_end_time = models.DateTimeField(verbose_name=_('Duel end time'), null=True, blank=True)

    active = models.BooleanField(verbose_name=_('Is duel active'),
                                 default='True', null=False, blank=False)

    @property
    def have_both_agreed(self):
        """

        :return: True if both photographers agreed to duel
        :rtype: Boolean
        """

        if self.agreed_a and self.agreed_b:
            return True
        else:
            return False

    def has_photographer_voted(self, p_photographer):
        """
        Returns True if p_photographer has already voted
        :param p_photographer: photographer in question
        :type p_photographer:
        :return:
        :rtype:
        """

        count_a = PhotoDuel.objects.filter(votes_a=p_photographer).count()
        count_b = PhotoDuel.objects.filter(votes_b=p_photographer).count()
        count_x = PhotoDuel.objects.filter(undecided=p_photographer).count()

        if count_a + count_b + count_x > 0:
            return True
        else:
            return False

    def is_photographer_contestant(self, p_photographer):
        """

        :param p_photographer: photographer
        :type p_photographer: Photographer
        :return: True is photographer is author of either photo in duel
        :rtype: Boolean
        """

        my_photographer_a = self.photo_a.author.get_my_photographer
        my_photographer_b = self.photo_b.author.get_my_photographer
        if (p_photographer.id == self.photo_a.author.get_my_photographer.id) or \
            (p_photographer.id == self.photo_b.author.get_my_photographer.id):
            return True
        else:
            return False

    def can_photographer_vote(self, p_photographer):
        """
        Main property - checks all conditions for voting
        :return: True if p_photographer can vote on duel
        :rtype: Boolean
        """

        if (not self.has_photographer_voted(p_photographer)) \
                and (not self.is_photographer_contestant(p_photographer)):
            return True
        else:
            return False

    def __unicode__(self):
        """

        :return: String representation of duel
        :rtype:
        """
        return "Duel <%s:%s>" % (self.photo_a.id ,self.photo_b.id)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    # loot = many to many field to Loot class, with through class LootAmount

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(PhotoDuel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Duel')
        verbose_name_plural = _('Duels')