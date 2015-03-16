from django.contrib import admin

from .models import (
    PhotoArtLover,
    Photographer,
    PhotoJudge,
    PhotoTeamManager,
)
# Register your models here.


class PhotoArtLoverAdmin(admin.ModelAdmin):

    list_display = ('member',
                    'name',
                    'level',
                    'current_xp',
                    'total_xp',
                    'character_type',
                    'character_active',
                    'created_at',
                    'updated_at',
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


class PhotoJudgeAdmin(admin.ModelAdmin):

    list_display = ('member',
                    'name',
                    'level',
                    'current_xp',
                    'total_xp',
                    'character_type',
                    'character_active',
                    'created_at',
                    'updated_at',
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


class PhotoTeamManagerAdmin(admin.ModelAdmin):

    list_display = ('member',
                    'name',
                    'level',
                    'current_xp',
                    'total_xp',
                    'character_type',
                    'character_active',
                    'created_at',
                    'updated_at',
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


class PhotographerAdmin(admin.ModelAdmin):

    list_display = ('member',
                    'name',
                    'level',
                    'current_xp',
                    'total_xp',
                    'character_type',
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

admin.site.register(PhotoArtLover, PhotoArtLoverAdmin)
admin.site.register(PhotoJudge, PhotoJudgeAdmin)
admin.site.register(PhotoTeamManager, PhotoTeamManagerAdmin)
admin.site.register(Photographer, PhotographerAdmin)