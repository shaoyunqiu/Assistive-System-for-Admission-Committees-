# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-09 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0048_student_readed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='send_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]