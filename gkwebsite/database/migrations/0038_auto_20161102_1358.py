# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-02 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0037_auto_20161101_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='stu_list',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='group',
            name='vol_list',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
