# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='url',
            field=models.URLField(default='https://www.test.com'),
            preserve_default=False,
        ),
    ]
