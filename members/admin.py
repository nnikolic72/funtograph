from django.contrib import admin

# Register your models here.
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'picture',
                    'created_at',
                    'updated_at',
                    'pk',
                    'id',
    )

    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('General Information', {'fields': [
            'user',
            'picture',
            'website'
        ]
        }
        ),
        ('Funtograph Information', {'fields': [
            'funtocredits',
            'current_energy',
            'max_energy',
        ]
        }
        ),
        ('Other handles', {'fields': [
            'instagram_handle',
            'instagram_handle_verified',
            'eyeem_handle',
            'eyeem_handle_verified',
            'flickr_handle',
            'flickr_handle_verified',
            'facebook_url',
            'facebook_url_verified',
            ]
        }
        ),
        ('Status Information', {'fields': [
            'suspended',
            'beta_tester'
        ]
        }
        ),
        ('Timestamps Information', {'fields': [
            'created_at',
            'updated_at'
        ]
        }
        ),


        ]


admin.site.register(Member, MemberAdmin)