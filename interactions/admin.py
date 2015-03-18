from django.contrib import admin

from .models import (
    Like,
    Comment,
    Favorite
)
# Register your models here.


class LikeAdmin(admin.ModelAdmin):
    """
    Admin Class for Likes model
    """

    list_display = ('photo',
                    'members_likers',
                    'created_at',
                    'updated_at',
    )

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        ('General Information', {'fields': [
            'photo',
            'members_likers',
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


class FavoriteAdmin(admin.ModelAdmin):
    """
    Admin Class for Favorites model
    """

    list_display = ('photo',
                    'members_favoriters',
                    'created_at',
                    'updated_at',
    )

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        ('General Information', {'fields': [
            'photo',
            'members_favoriters',
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


class CommentAdmin(admin.ModelAdmin):
    """
    Admin Class for Comment model
    """

    list_display = ('photo',
                    'members_commenters',
                    'comment_text',
                    'created_at',
                    'updated_at',
    )

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        ('General Information', {'fields': [
            'photo',
            'members_commenters',
            'comment_text',
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


admin.site.register(Like, LikeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Comment, CommentAdmin)