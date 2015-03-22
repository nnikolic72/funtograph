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
            'character_type'
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

        ('Timestamps', {'fields': [
            'created_at',
            'updated_at'
        ]
        }
        ),

        ]


admin.site.register(Photographer, PhotographerAdmin)