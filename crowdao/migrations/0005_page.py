# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-11 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdao', '0004_auto_20161011_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=255, verbose_name='Subtitle')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('image', models.FileField(blank=True, upload_to='', verbose_name='Image or video')),
                ('slug', models.CharField(blank=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['title', 'slug'],
            },
        ),
    ]
