from django.contrib import admin
from info.models import Headmate

class HeadmateAdmin(admin.ModelAdmin):

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

admin.site.register(Headmate, HeadmateAdmin)