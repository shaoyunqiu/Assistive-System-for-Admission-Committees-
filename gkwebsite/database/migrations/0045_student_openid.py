# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0044_auto_20161104_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='openid',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
