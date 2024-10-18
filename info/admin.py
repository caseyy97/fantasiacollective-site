from django.contrib import admin
from solo.admin import SingletonModelAdmin
from info.models import SiteConfig, Headmate
from django_summernote.widgets import SummernoteWidget
from django.db import models

def get_site_name():
    name = SiteConfig.objects.get().name
    return name

class SiteConfigAdmin(SingletonModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }

class HeadmateAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
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
admin.site.site_header = get_site_name()
admin.site.site_title = get_site_name()
admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(Headmate, HeadmateAdmin)