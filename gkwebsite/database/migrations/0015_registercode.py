# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_volunteer_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerCode', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.IntegerField(blank=True, default=0)),
                ('account', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
