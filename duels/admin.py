from django.contrib import admin

from .models import PhotoDuel


# Register your models here.
class PhotoDuelAdmin(admin.ModelAdmin):
    """
    Admin class for basic Photo Duel
    """

    def restart_duel(self, request, queryset):
        """
        Action -> Clears duel result and restarts it
        :return:
        :rtype:
        """
        l_votes_cnt = 0
        l_duel_cnt = 0

        for duel in queryset:
            l_duel_cnt += 1
            for votes in duel.votes_a.all():
                duel.votes_a.remove(votes)
                l_votes_cnt += 1
            for votes in duel.votes_b.all():
                duel.votes_b.remove(votes)
                l_votes_cnt += 1
            for votes in duel.undecided.all():
                duel.undecided.remove(votes)
                l_votes_cnt += 1

        buf = "Restarted %s duels and deleted total of %s votes." % (l_duel_cnt, l_votes_cnt)
        self.message_user(request, buf)
    restart_duel.short_description = 'Restart duels'

    actions = (restart_duel,)

    list_display = ('photo_a',
                    'photo_b',
                    'agreed_a',
                    'agreed_b',
                    'winner',
                    'created_at',
                    'pk',
    )

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        ('General Information', {'fields': [
            'photo_a',
            'photo_b',
            'agreed_a',
            'agreed_b',
            'active',
            'created_at',
            'updated_at',
        ]
        }
        ),

        ('Voting', {'fields': [
            'votes_a',
            'votes_b',
            'undecided',
            'winner',
            'duel_start_time',
            'duel_end_time',
        ]
        }
        ),
        ]

admin.site.register(PhotoDuel, PhotoDuelAdmin)