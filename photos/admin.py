from django.contrib import admin

from .models import (
    Photo,
    PhotoCategory,
    PhotoAttribute,
    PhotoToPhotographer
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


class OwnerInline(admin.TabularInline):
    model = PhotoToPhotographer
    fields = ('photographer',)

class PhotoAdmin(admin.ModelAdmin):

    inlines = (OwnerInline,)

    list_display = ('title',
                    'photo',
                    'avg_photo_rating',
                    'photo_wear',
                    'active',
                    'for_sale'
    )

    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ('categories', 'attributes', )

    fieldsets = [
        ('General Information', {'fields': [
            'title',
            'photo',
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

        ('In-game Information', {'fields': [
            'photo_wear',
            'avg_photo_rating',
            'photo_price',
            'for_sale',
            'photo',

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