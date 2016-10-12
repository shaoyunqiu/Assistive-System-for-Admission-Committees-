# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-11 09:43
from __future__ import unicode_literals

import database.my_field
import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20161010_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\d|\\w){4,}$')])),
                ('password', models.CharField(default='12345678', max_length=50, validators=[django.core.validators.RegexValidator(regex='^(\\d|\\w){4,}$')])),
                ('realName', models.CharField(blank=True, default='', max_length=20)),
                ('birth', models.DateField(blank=True, default=datetime.date.today)),
                ('idNumber', models.CharField(blank=True, default='', max_length=40, validators=[django.core.validators.RegexValidator(regex='^(\\d|\\w){18}$')])),
                ('type', models.IntegerField(blank=True, default=-1)),
                ('sex', models.IntegerField(blank=True, default=-1)),
                ('nation', models.IntegerField(blank=True, default=-1)),
                ('school', models.CharField(blank=True, default='', max_length=200)),
                ('classroom', models.CharField(blank=True, default='', max_length=20)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('phone', models.CharField(blank=True, default='', max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\d)+$')])),
                ('email', models.CharField(blank=True, default='', max_length=50, validators=[django.core.validators.EmailValidator()])),
                ('dadPhone', models.CharField(blank=True, default='', max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\d)+$')])),
                ('momPhone', models.CharField(blank=True, default='', max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\d)+$')])),
                ('tutorName', models.CharField(blank=True, default='', max_length=20)),
                ('tutorPhone', models.CharField(blank=True, default='', max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\d)+$')])),
                ('province', models.IntegerField(blank=True, default=-1)),
                ('major', models.IntegerField(blank=True, default=-1)),
                ('testScoreList', database.my_field.ListField(blank=True, default=[])),
                ('rankList', database.my_field.ListField(blank=True, default=[])),
                ('sumNumberList', database.my_field.ListField(blank=True, default=[])),
                ('estimateScore', models.IntegerField(blank=True, default=-1)),
                ('realScore', models.IntegerField(blank=True, default=-1)),
                ('admissionStatus', models.IntegerField(blank=True, default=-1)),
                ('comment', models.TextField(blank=True, default='')),
                ('registerCode', models.CharField(blank=True, default='', max_length=100)),
                ('teacherList', database.my_field.ListField(blank=True, default=[])),
                ('volunteerAccountList', database.my_field.ListField(blank=True, default=[])),
                ('isLogedin', models.IntegerField(blank=True, default=0)),
                ('isRegistered', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
