from django.contrib import admin

from .models import (

    Photographer,
)
# Register your models here.


class PhotographerAdmin(admin.ModelAdmin):

    list_display = ('member',
                    'name',
                    'level',
                    'current_xp',
                    'total_xp',

                    'character_active',
                    'created_at',
                    'updated_at',
                    'pk'
    )

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        ('General Information', {'fields': [
            'member',
            'name',
            'level',
        ]
        }
        ),

        ('In-game information', {'fields': [
            'current_xp',
            'total_xp',
            'character_active'
        ]
        }
        ),

        ('In-game permissions', {'fields': [
            'allowed_to_duel',
            'allowed_to_team_duel',
            'allowed_to_join_league',
            'allowed_to_found_collective',
            'allowed_to_like',
            'allowed_to_comment',
            'allowed_to_favorite',
            'allowed_to_see_stats',
        ]
        }
        ),

        ('Timestamps', {'fields': [
            'created_at',
            'updated_at'
        ]
        }
        ),

        ]


admin.site.register(Photographer, PhotographerAdmin)