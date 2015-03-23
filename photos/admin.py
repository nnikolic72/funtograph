from django.contrib import admin
from members.models import Member

from .models import (
    Photo,
    PhotoCategory,
    PhotoAttribute,
)

# Register your models here.


class PhotoCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for PhotoCategory data model
    """

    list_display = ('name',
                    'slug',
                    'created_at',
                    'updated_at'
    )

    readonly_fields = ('created_at', 'updated_at')

    prepopulated_fields = {'slug': ('name',)}


class PhotoAttributeAdmin(admin.ModelAdmin):
    """
    Admin interface for PhotoCategory data model
    """

    list_display = ('name',
                    'slug',
                    'created_at',
                    'updated_at'
    )

    readonly_fields = ('created_at', 'updated_at')

    prepopulated_fields = {'slug': ('name',)}


#class OwnerInline(admin.TabularInline):
#    model = Member
#    fields = ('photographer',)

class PhotoAdmin(admin.ModelAdmin):

    #inlines = (OwnerInline,)

    list_display = ('title',
                    'photo',
                    'author',
                    'avg_photo_rating',
                    'photo_wear',
                    'active',
                    'for_sale',
                    'photo_price',
    )

    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ('categories', 'attributes', )

    fieldsets = [
        ('General Information', {'fields': [
            'title',
            'photo',
            'author',
            'owner',
            'active',
        ]
        }
        ),

        ('Photo properties', {'fields': [
            'categories',
            'attributes',
        ]
        }
        ),

        ('EXIF and Cloudinary Information', {'fields': [
            'phash',
            'format',
            'dominant_color',
            'full_url',
            'photo_creation_date',
            'creator_tool',
            'lens_model',
            'camera_make',
            'camera_model',

        ]
        }
        ),

        ('In-game Information', {'fields': [
            'photo_wear',
            'avg_photo_rating',
            'photo_price',
            'for_sale',
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

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoCategory, PhotoCategoryAdmin)
admin.site.register(PhotoAttribute, PhotoAttributeAdmin)