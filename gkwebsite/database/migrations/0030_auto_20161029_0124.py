# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-28 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0029_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dadName',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='momName',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
