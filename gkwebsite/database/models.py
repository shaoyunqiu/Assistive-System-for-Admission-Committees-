from __future__ import unicode_literals

from django.db import models
import my_field
import django.core.validators

# Create your models here.

class Teacher(models.Model):
    account = models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex=r'(\d|\w){4,}')])
    # bug here, sometimes validation check invalid
    password = models.CharField(max_length=50,default="12345678")
    realName = models.CharField(max_length=20,default='')
    phone = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=50,default='')
    area = models.CharField(max_length=50,default='')
    volunteerList = my_field.ListField(default=[])

    def __unicode__(self):
        varList = (vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self,item,'None')) + ' || '
        return ret
