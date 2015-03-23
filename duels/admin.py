from django.contrib import admin

from .models import PhotoDuel


# Register your models here.
class PhotoDuelAdmin(admin.ModelAdmin):
    """
    Admin class for basic Photo Duel
    """

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