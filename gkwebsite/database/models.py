# coding:utf8

from __future__ import unicode_literals

from django.db import models
import my_field
import django.core.validators
import datetime


# Create your models here.

class Teacher(models.Model):
    account = models.CharField(max_length=50, unique=True,
                               validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # account validation : 4个或以上的数字或字母
    password = models.CharField(max_length=50, default="12345678",
                                validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # password validation : 4个或以上的数字或字母
    realName = models.CharField(max_length=20, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True,
                             validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])
    email = models.CharField(max_length=50, default='', blank=True,
                             validators=[django.core.validators.EmailValidator()])
    area = models.CharField(max_length=50, default='', blank=True)
    volunteerList = my_field.ListField(default=[], blank=True)

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret


class Student(models.Model):
    account = models.CharField(max_length=50, unique=True,
                               validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # account validation : 4个或以上的数字或字母
    password = models.CharField(max_length=50, default="12345678",
                                validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # password validation : 4个或以上的数字或字母
    realName = models.CharField(max_length=20, default='', blank=True)
    birth = models.DateField(default=datetime.date.today, blank=True)
    idNumber = models.CharField(max_length=40, default='', blank=True,
                                validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){18}$')])
    # idNumber validation : 18个数字或字母
    type = models.IntegerField(default=-1, blank=True)
    sex = models.IntegerField(default=-1, blank=True)
    nation = models.IntegerField(default=-1, blank=True)
    school = models.CharField(max_length=200, default='', blank=True)
    classroom = models.CharField(max_length=20, default='', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True,
                             validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])
    email = models.CharField(max_length=50, default='', blank=True,
                             validators=[django.core.validators.EmailValidator()])
    dadPhone = models.CharField(max_length=20, default='', blank=True,
                                validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])
    momPhone = models.CharField(max_length=20, default='', blank=True,
                                validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])
    tutorName = models.CharField(max_length=20, default='', blank=True)
    tutorPhone = models.CharField(max_length=20, default='', blank=True,
                                  validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])
    province = models.IntegerField(default=-1, blank=True)
    major = models.IntegerField(default=-1, blank=True)
    testScoreList = my_field.ListField(default=[], blank=True)
    rankList = my_field.ListField(default=[], blank=True)
    sumNumberList = my_field.ListField(default=[], blank=True)
    estimateScore = models.IntegerField(default=-1, blank=True)
    realScore = models.IntegerField(default=-1, blank=True)
    admissionStatus = models.IntegerField(default=-1, blank=True)
    comment = models.TextField(default='', blank=True)
    registerCode = models.CharField(max_length=100, default='', blank=True)
    teacherList = my_field.ListField(default=[], blank=True)
    volunteerAccountList = my_field.ListField(default=[], blank=True)
    isLogedin = models.IntegerField(default=0, blank=True)
    isRegistered = models.IntegerField(default=0, blank=True)

    ID = 'id'

    ACCOUNT = 'account'
    PASSWORD = 'password'
    REAL_NAME = 'realName'
    BIRTH = 'birth'
    ID_NUMBER = 'idNumber'

    TYPE = 'type'
    SEX = 'sex'
    NATION = 'nation'
    SCHOOL = 'school'
    CLASSROOM = 'classroom'

    ADDRESS = 'address'
    PHONE = 'phone'
    EMAIL = 'email'
    DAD_PHONE = 'dadPhone'
    MOM_PHONE = 'momPhone'

    TUTOR_NAME = 'tutorName'
    TUTOR_PHONE = 'tutorPhone'
    PROVINCE = 'province'
    MAJOR = 'major'
    TEST_SCORE_LIST = 'testScoreList'

    RANK_LIST = 'rankList'
    SUM_NUMBER_LIST = 'sumNumberList'
    ESTIMATE_SCORE = 'estimateScore'
    REAL_SCORE = 'realScore'
    ADMISSION_STATUS = 'admissionStatus'

    COMMENT = 'comment'
    REGISTER_CODE = 'registerCode'
    TEACHER_LIST = 'teacherList'
    VOLUNTEER_ACCOUNT_LIST = 'volunteerAccountList'
    IS_LOGED_IN = 'isLogedin'

    IS_REGISTERED = 'isRegistered'

    FIELD_LIST = [ID,
                  ACCOUNT, PASSWORD, REAL_NAME, BIRTH, ID_NUMBER,
                  TYPE, SEX, NATION, SCHOOL, CLASSROOM,
                  ADDRESS, PHONE, EMAIL, DAD_PHONE, MOM_PHONE,
                  TUTOR_NAME, TUTOR_PHONE, PROVINCE, MAJOR, TEST_SCORE_LIST,
                  RANK_LIST, SUM_NUMBER_LIST, ESTIMATE_SCORE, REAL_SCORE, ADMISSION_STATUS,
                  COMMENT, REGISTER_CODE, TEACHER_LIST, VOLUNTEER_ACCOUNT_LIST, IS_LOGED_IN,
                  IS_REGISTERED]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Student._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret