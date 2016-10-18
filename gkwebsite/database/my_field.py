# coding:utf8

from django.db import models
import ast

MAJOR_LIST = [u'计算机科学与技术系', u'电子工程系', u'自动化系', u'化学系', u'物理系']
SEX_LIST = [u'男', u'女']
PROVINCE_LIST = [u'北京', u'上海', u'内蒙古', u'江苏', u'湖北', u'广东', u'广西']

def majorIntToString(num):
    index = num % len(MAJOR_LIST)
    return MAJOR_LIST[index]

def sexIntToString(num):
    index = num % len(SEX_LIST)
    return SEX_LIST[index]

def provinceIntToString(num):
    index = num % len(PROVINCE_LIST)
    return PROVINCE_LIST[index]



class ListField(models.TextField):
    #__metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)  # use str(value) in Python 3

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
