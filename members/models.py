from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

import cloudinary

from characters.models import (
    PhotoArtLover,
    Photographer,
    PhotoJudge,
    PhotoTeamManager
)

# Create your models here.


class MembershipType(models.Model):
    """
    Types of memberships
    """

    FREE_MEMBERSHIP = 1
    PAID_MEMBERSHIP = 2
    TRIAL_MEMBERSHIP = 2

    MEMBERSHIP_FEES_TYPES = (
        (FREE_MEMBERSHIP, _('Free Membership')),
        (PAID_MEMBERSHIP, _('Paid Membership')),
    )

    RECURRING_MEMBERSHIP = 1
    NON_RECURRING_MEMBERSHIP = 2

    MEMBERSHIP_RECURRING_TYPES = (
        (RECURRING_MEMBERSHIP, _('Recurring Membership')),
        (NON_RECURRING_MEMBERSHIP, _('Non-recurring Membership')),
    )
    membership_type_name = models.CharField(max_length=100, null=False, blank=False)
    membership_fee_type = models.CharField(max_length=10, choices=MEMBERSHIP_FEES_TYPES)
    membership_recurring_type = models.CharField(max_length=10, choices=MEMBERSHIP_RECURRING_TYPES)
    active = models.BooleanField(default=True, null=False, blank=False)

    # membership cost
    membership_fee_price = models.FloatField(blank=False, null=False, default=0)

    # membership duration in days
    DURATION_TRIAL = 15
    DURATION_MONTHLY = 30
    DURATION_YEARLY = 365

    MEMBERSHIP_DURATIONS = (
        (DURATION_TRIAL, _('Trial membership period')),
        (DURATION_MONTHLY, _('Monthly membership')),
        (DURATION_YEARLY, _('Yearly membership')),
    )
    membership_duration = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.membership_name

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(MembershipType, self).save(*args, **kwargs)

    class Meta:
        ordering = [_('membership_type_name')]
        verbose_name = _('MembershipType')
        verbose_name_plural = _('MembershipTypes')


class Member(models.Model):
    """
    Defines Member data model
    """

    @property
    def get_my_photo_art_lover(self):
        """

        :return: PhotoArtLover object
        :rtype:
        """

        try:
            my_photo_art_lover = PhotoArtLover.objects.get(member=self)
        except ObjectDoesNotExist:
            my_photo_art_lover = None

        return my_photo_art_lover

    @property
    def get_my_photographer(self):
        """

        :return: Photographer object
        :rtype:
        """

        try:
            my_photographer = Photographer.objects.get(member=self)
        except ObjectDoesNotExist:
            my_photographer = None

        return my_photographer

    @property
    def get_my_photo_judge(self):
        """

        :return: Photographer object
        :rtype:
        """

        try:
            my_photo_judge = PhotoJudge.objects.get(member=self)
        except ObjectDoesNotExist:
            my_photo_judge = None

        return my_photo_judge

    @property
    def get_my_photo_team_manager(self):
        """

        :return: Photographer object
        :rtype:
        """

        try:
            my_photo_team_manager = PhotoTeamManager.objects.get(member=self)
        except ObjectDoesNotExist:
            my_photo_team_manager = None

        return my_photo_team_manager


    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True, null=True,
                              verbose_name=_('Web Site URL'),
                              help_text=_('Your web site URL')
                              )
    picture = cloudinary.models.CloudinaryField('image', null=True
                                                )
    instagram_handle = models.CharField(max_length=30, null=True, blank=True,
                                        verbose_name=_('Instagram user name'),
                                        help_text=_('Your Instagram account user name')
    )
    eyeem_handle = models.CharField(max_length=30, null=True, blank=True,
                                    verbose_name=_('EyeEm user name'),
                                    help_text=_('Your EyeEm account user name')
    )
    flickr_handle = models.CharField(max_length=30, null=True, blank=True,
                                     verbose_name=_('Flickr user name'),
                                     help_text=_('Your Flickr account user name')
    )
    facebook_url = models.CharField(max_length=30, null=True, blank=True,
                                    verbose_name=_('Facebook account URL'),
                                    help_text=_('Your Facebook profile URL')
    )
    instagram_handle_verified = models.BooleanField(default=False, null=False, blank=False,
                                                    verbose_name=_('Instagram handle verified'),
                                                    help_text=_('Checked if mods verified member''s Instagram handle')
    )
    eyeem_handle_verified = models.BooleanField(default=False, null=False, blank=False,
                                                verbose_name=_('EyeEm handle verified'),
                                                help_text=_('Checked if mods verified member''s EyeEm handle')
    )
    flickr_handle_verified = models.BooleanField(default=False, null=False, blank=False,
                                                verbose_name=_('Flickr handle verified'),
                                                help_text=_('Checked if mods verified member''s Flickr handle')
    )
    facebook_url_verified = models.BooleanField(default=False, null=False, blank=False,
                                                verbose_name=_('Facebook URL verified'),
                                                help_text=_('Checked if mods verified member''s Facebook URL')
    )

    funtocredits = models.IntegerField(default=0, null=False, blank=False,
                                       verbose_name=_('FuntoCredits'),
                                       help_text=_('How much FuntoCredits Member has')
    )

    suspended = models.BooleanField(default=False, null=False, blank=False,
                                    verbose_name=_('Suspended'),
                                    help_text=_('Checked if Member is suspended')
    )
    beta_tester = models.BooleanField(default=False, null=False, blank=False,
                                    verbose_name=_('Beta tester'),
                                    help_text=_('Checked if Member is Beta tester')
    )

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def is_member_active(self):
        if self.suspended:
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']
        verbose_name = _('Member')
        verbose_name_plural = _('Members')


class Membership(models.Model):
    """
    Model that stores data about one purchased or free membership
    """

    member = models.ForeignKey(Member, null=True, blank=True,
                               verbose_name=_('Membership Owner'),
                               help_text=_('Foreign key to Member object')
    )

    membership_start_time = models.DateTimeField(null=False, blank=False,
                                                 verbose_name=_('Membership Start Time'),
                                                 help_text=_('Date and time when the membership starts')
    )

    membership_end_time = models.DateTimeField(null=False, blank=False,
                                               verbose_name=_('Membership End Time'),
                                               help_text=_('Date and time when the membership ends')
    )

    membership_type = models.ForeignKey(MembershipType, null=True, blank=True,
                                        verbose_name=_('Membership Type'),
                                        help_text=_('Membership type')
    )

    # only one membership can be active per member
    active_membership = models.BooleanField(default=False, null=False, blank=False,
                                            verbose_name=_('Is membership active'),
                                            help_text=_(
                                                'Checked if membership is active. Only one membership per member allowed'
                                            )
    )
    suspended_membership = models.BooleanField(default=False, null=False, blank=False,
                                    verbose_name=_('Suspended Membership'),
                                    help_text=_('Checked if Membership is suspended')
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def is_membership_active(self):
        if self.active_membership:
            return self.active_membership
        else:
            return False

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Membership, self).save(*args, **kwargs)

    class Meta:
        ordering = ['membership_end_time']
        verbose_name = _('Membership')
        verbose_name_plural = _('Memberships')


