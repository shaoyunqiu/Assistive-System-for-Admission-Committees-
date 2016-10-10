#coding:utf8

from __future__ import unicode_literals

from django.db import models
import my_field
import django.core.validators

# Create your models here.

class Teacher(models.Model):
    account = models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # account validation : 4个或以上的数字或字母
    password = models.CharField(max_length=50,default="12345678", validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # password validation : 4个或以上的数字或字母
    realName = models.CharField(max_length=20,default='',blank=True)
    phone = models.CharField(max_length=20,default='', blank=True, validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])
    email = models.CharField(max_length=50,default='', blank=True, validators=[django.core.validators.EmailValidator()])
    area = models.CharField(max_length=50,default='', blank=True)
    volunteerList = my_field.ListField(default=[], blank=True)

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self,item,'None')) + ' || '
        return ret
