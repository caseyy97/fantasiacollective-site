# Generated by Django 5.1.1 on 2024-10-18 08:19

import info.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headmate',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pronouns', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to=info.models.Headmate.file_directory)),
                ('image_source', models.URLField(blank=True)),
                ('icon', models.ImageField(blank=True, upload_to=info.models.Headmate.file_directory)),
                ('custom_colour_enabled', models.BooleanField(default=False, verbose_name='Enable custom colours')),
                ('bg_colour', models.CharField(blank=True, help_text="Hexadecimal colour code, i.e., '#FF0000'.", max_length=7, verbose_name='Background colour')),
                ('border_colour', models.CharField(blank=True, help_text="Hexadecimal colour code, i.e., '#FF0000'.", max_length=7, verbose_name='Border colour')),
                ('shadow_colour', models.CharField(blank=True, help_text="Hexadecimal colour code, i.e., '#FF0000'.", max_length=7, verbose_name='Shadow colour')),
                ('display', models.BooleanField(default=True, help_text='Display this headmate on the frontend.', verbose_name='Show headmate')),
                ('order', models.SmallIntegerField(blank=True, verbose_name='Sort order')),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Fantasia Collective', max_length=50)),
                ('favicon', models.ImageField(blank=True, upload_to='')),
                ('header_image', models.ImageField(blank=True, upload_to='')),
                ('header_info', models.TextField(blank=True)),
                ('footer_info', models.TextField(blank=True)),
                ('bg_colour', models.CharField(help_text="Hexadecimal colour code, i.e., '#FF0000'.", max_length=7, verbose_name='Background colour')),
                ('last_updated', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
