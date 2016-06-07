# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 16:19
from __future__ import unicode_literals

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image_url', stdimage.models.StdImageField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('examples1', stdimage.models.StdImageField(blank=True, upload_to='')),
                ('examples2', stdimage.models.StdImageField(blank=True, upload_to='')),
                ('examples3', stdimage.models.StdImageField(blank=True, upload_to='')),
            ],
        ),
    ]
