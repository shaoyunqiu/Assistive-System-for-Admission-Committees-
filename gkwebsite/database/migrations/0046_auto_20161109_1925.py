# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-09 11:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0045_student_openid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='send',
            new_name='teacher_id',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='receive_vol',
        ),
        migrations.AddField(
            model_name='notice',
            name='send_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='notice',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='wechaturl',
            name='text',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='wechaturl',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='notice',
            name='receive_stu',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='wechaturl',
            name='message_url',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='wechaturl',
            name='picture_url',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
