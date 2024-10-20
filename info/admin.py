from django.contrib import admin
from solo.admin import SingletonModelAdmin
from info.models import SiteConfig, Headmate
from martor.widgets import AdminMartorWidget

class SiteConfigAdmin(SingletonModelAdmin):

    formfield_overrides = {
        SiteConfig.header_info: {'widget': AdminMartorWidget},
        SiteConfig.footer_info: {'widget': AdminMartorWidget},
    }

class HeadmateAdmin(admin.ModelAdmin):

    formfield_overrides = {
        Headmate.bio: {'widget': AdminMartorWidget},
    }

    fieldsets = [
        (
            "Basic Info",
            {
                "fields": ["name", "pronouns", "age", "bio"],
            },
        ),
        (
            "Image and Icon",
            {
                "fields": ["image", "image_source", "icon"],
            }
        ),
        (
            "Custom Colours",
            {
                "fields": ["custom_colour_enabled", "bg_colour", "border_colour", "shadow_colour"],
            }
        ),
        (
            "Display Settings",
            {
                "fields": ["display", "order"],
            }
        ),
    ]

    list_display = ("name", "display", "order")
    ordering = ("order", )

# Register your models here.
admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(Headmate, HeadmateAdmin)