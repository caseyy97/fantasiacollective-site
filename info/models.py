from django.db import models
from solo.models import SingletonModel

# Create your models here.
class SiteConfig(SingletonModel):
    name = models.CharField(max_length=50, default="Fantasia Collective")
    favicon = models.ImageField(blank=True, name="favicon")
    header_image = models.ImageField(blank=True)
    header_info = models.TextField(blank=True)
    footer_info = models.TextField(blank=True)
    bg_colour = models.CharField(verbose_name="Background colour", max_length=7, help_text="Hexadecimal colour code, i.e., '#FF0000'.")
    # maintenance_mode = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return "Site config"

class Headmate(models.Model):
    # basic info
    name = models.CharField(primary_key=True, max_length=50)
    pronouns = models.CharField(max_length=25)
    age = models.CharField(max_length=25)
    bio = models.TextField()
    
    # image and icon
    def file_directory(self, filename):
        return f"headmates/{self.name.lower}/{filename}"
    
    image = models.ImageField(upload_to=file_directory)
    image_source = models.URLField(blank=True)
    icon = models.ImageField(upload_to=file_directory, blank=True)

    # custom colours
    custom_colour_enabled = models.BooleanField(verbose_name="Enable custom colours", default=False)
    bg_colour     = models.CharField(verbose_name="Background colour", max_length=7, blank=True, help_text="Hexadecimal colour code, i.e., '#FF0000'.")
    border_colour = models.CharField(verbose_name="Border colour", max_length=7, blank=True, help_text="Hexadecimal colour code, i.e., '#FF0000'.")
    shadow_colour = models.CharField(verbose_name="Shadow colour", max_length=7, blank=True, help_text="Hexadecimal colour code, i.e., '#FF0000'.")

    # display settings
    display = models.BooleanField(verbose_name="Show headmate", default=True, help_text="Display this headmate on the frontend.")
    order = models.SmallIntegerField(verbose_name="Sort order", blank=True)

    def __str__(self):
        return self.name