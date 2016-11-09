# coding:utf8

from __future__ import unicode_literals

from django.db import models
from django import forms

import my_field
import django.core.validators
import datetime


# Create your models here.

class Teacher(models.Model):
    account = models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # account validation : 4个或以上的数字或字母
    password = models.CharField(max_length=50, default="12345678", validators=[django.core.validators.RegexValidator(regex=r'^(\S){4,}$')])
    # password validation : 4个或以上的数字或字母
    realName = models.CharField(max_length=20, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True, validators=[django.core.validators.RegexValidator(regex=r'^(\d)+$')])

    email = models.CharField(max_length=50, default='', blank=True, validators=[django.core.validators.EmailValidator()])
    area = models.CharField(max_length=50, default='', blank=True)
    volunteerList = my_field.ListField(default=[], blank=True)
    wechat = models.CharField(max_length=50, default='', blank=True)
    fixedPhone = models.CharField(max_length=50, default='', blank=True)
    comment = models.TextField(default='', blank=True)

    ID = 'id'
    ACCOUNT = 'account'
    PASSWORD = 'password'
    REAL_NAME = 'realName'
    PHONE = 'phone'
    EMAIL = 'email'

    AREA = 'area'
    VOLUNTEER_LIST = 'volunteerList'
    WECHAT = 'wechat'
    FIXED_PHONE = 'fixedPhone'
    COMMENT = 'comment'

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
    account = models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # account validation : 4个或以上的数字或字母
    password = models.CharField(max_length=50, default="12345678", validators=[django.core.validators.RegexValidator(regex=r'^(\S){4,}$')])
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
    major = my_field.ListField(default=[], blank=True)
    testScoreList = my_field.ListField(default=[], blank=True)
    rankList = my_field.ListField(default=[], blank=True)
    sumNumberList = my_field.ListField(default=[], blank=True)
    estimateScore = models.TextField(default='{}', blank=True)
    realScore = models.IntegerField(default=-1, blank=True)
    admissionStatus = models.CharField(max_length=50, default='', blank=True)
    comment = models.TextField(default='', blank=True)
    registerCode = models.CharField(max_length=100, default='', blank=True)
    teacherList = my_field.ListField(default=[], blank=True)
    volunteerAccountList = my_field.ListField(default=[], blank=True)
    isLogedin = models.IntegerField(default=0, blank=True)
    isRegistered = models.IntegerField(default=0, blank=True)
    groupList = my_field.ListField(default=[], blank=True)
    wechat = models.CharField(max_length=50, default='', blank=True)
    fixedPhone = models.CharField(max_length=50, default='', blank=True)
    qq = models.CharField(max_length=50, default='', blank=True)
    dadName = models.CharField(max_length=50, default='', blank=True)
    momName = models.CharField(max_length=50, default='', blank=True)

    duiyingTeacher = models.CharField(max_length=500, default='', blank=True)

    quanxian = models.IntegerField(default=1, blank=True)

    openid = models.CharField(max_length=500, default='', blank=True)

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
    GROUP_LIST = 'groupList'
    WECHAT = 'wechat'
    FIXED_PHONE = 'fixedPhone'
    QQ = 'qq'

    DAD_NAME = 'dadName'
    MOM_NAME = 'momName'
    DUIYING_TEACHER = 'duiyingTeacher'
    QUANXIAN = 'quanxian'
    OPEN_ID = 'openid'


    FIELD_LIST = [ID,
                  ACCOUNT, PASSWORD, REAL_NAME, BIRTH, ID_NUMBER,
                  TYPE, SEX, NATION, SCHOOL, CLASSROOM,
                  ADDRESS, PHONE, EMAIL, DAD_PHONE, MOM_PHONE,
                  TUTOR_NAME, TUTOR_PHONE, PROVINCE, MAJOR, TEST_SCORE_LIST,
                  RANK_LIST, SUM_NUMBER_LIST, ESTIMATE_SCORE, REAL_SCORE, ADMISSION_STATUS,
                  COMMENT, REGISTER_CODE, TEACHER_LIST, VOLUNTEER_ACCOUNT_LIST, IS_LOGED_IN,
                  IS_REGISTERED, GROUP_LIST, WECHAT, FIXED_PHONE,QQ,
                  DAD_NAME, MOM_NAME, DUIYING_TEACHER, QUANXIAN, OPEN_ID]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Student._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret

class Volunteer(models.Model):
    account = models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex=r'^(\d|\w){4,}$')])
    # account validation : 4个或以上的数字或字母
    password = models.CharField(max_length=50, default="12345678", validators=[django.core.validators.RegexValidator(regex=r'^(\S){4,}$')])
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
    major = my_field.ListField(default=[], blank=True)
    testScoreList = my_field.ListField(default=[], blank=True)
    rankList = my_field.ListField(default=[], blank=True)
    sumNumberList = my_field.ListField(default=[], blank=True)
    estimateScore = models.CharField(max_length=2000, default='', blank=True)
    realScore = models.IntegerField(default=-1, blank=True)
    admissionStatus = models.CharField(max_length=50, default='', blank=True)
    comment = models.TextField(default='', blank=True)
    registerCode = models.CharField(max_length=100, default='', blank=True)
    teacherList = my_field.ListField(default=[], blank=True) #对应的老师
    studentAccountList = my_field.ListField(default=[], blank=True)
    isLogedin = models.IntegerField(default=0, blank=True)
    isRegistered = models.IntegerField(default=0, blank=True)
    student_id = models.CharField(max_length=100, default='', blank=True) #学生卡卡号
    groupList = my_field.ListField(default=[], blank=True) #分管的组
    wechat = models.CharField(max_length=50, default='', blank=True)
    fixedPhone = models.CharField(max_length=50, default='', blank=True)
    qq = models.CharField(max_length=50, default='', blank=True)

    quanxian = models.IntegerField(default=0, blank=True)

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
    STUDENT_ACCOUNT_LIST = 'studentAccountList'
    IS_LOGED_IN = 'isLogedin'

    IS_REGISTERED = 'isRegistered'
    STUDENT_ID = 'student_id'
    GROUP_LIST = 'groupList'
    WECHAT = 'wechat'
    FIXED_PHONE = 'fixedPhone'

    QQ = 'qq'
    QUANXIAN = 'quanxian'

    FIELD_LIST = [ID,
                  ACCOUNT, PASSWORD, REAL_NAME, BIRTH, ID_NUMBER,
                  TYPE, SEX, NATION, SCHOOL, CLASSROOM,
                  ADDRESS, PHONE, EMAIL, DAD_PHONE, MOM_PHONE,
                  TUTOR_NAME, TUTOR_PHONE, PROVINCE, MAJOR, TEST_SCORE_LIST,
                  RANK_LIST, SUM_NUMBER_LIST, ESTIMATE_SCORE, REAL_SCORE, ADMISSION_STATUS,
                  COMMENT, REGISTER_CODE, TEACHER_LIST, STUDENT_ACCOUNT_LIST, IS_LOGED_IN,
                  IS_REGISTERED,STUDENT_ID, GROUP_LIST, WECHAT, FIXED_PHONE,
                  QQ, QUANXIAN]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Volunteer._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret

class RegisterCode(models.Model):
    registerCode = models.CharField(max_length=100, default='', blank=True)
    state = models.IntegerField(default=0, blank=True)
    account = models.CharField(max_length=100, default='', blank=True)

    REGISTER_CODE = 'registerCode'
    STATE = 'state'
    ACCOUNT = 'account'

    FIELD_LIST = [REGISTER_CODE, STATE, ACCOUNT]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in RegisterCode._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret

class Picture(models.Model):


    year = models.IntegerField(default=0, blank=True) #年份
    province = models.IntegerField(default=0, blank=True) #省份
    subject = models.IntegerField(default=0, blank=True) #科目
    number = models.IntegerField(default=0, blank=True) #题号
    score = models.IntegerField(default=0, blank=True) #得分
    category = models.IntegerField(default=0, blank=True) #主观客观

    isTitle = models.IntegerField(default=0, blank=True) #是否是纯标题
    isDelivered = models.IntegerField(default=0, blank=True) #是否发布

    ID = 'id'

    YEAR = 'year'
    PROVINCE = 'province'
    SUBJECT = 'subject'
    NUMBER = 'number'
    SCORE = 'score'
    CATEGORY = 'category'

    IS_TITLE = 'isTitle'
    IS_DELEVERED = 'isDelivered'

    FIELD_LIST = [ID, YEAR, PROVINCE, SUBJECT, NUMBER, SCORE, CATEGORY, IS_TITLE, IS_DELEVERED]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Picture._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret

class Notice(models.Model):
    title = models.CharField(max_length=300, default='', blank=True)
    text = models.TextField(default='', blank=True)
    teacher_id = models.CharField(max_length=300, default='', blank=True)
    send_date = models.DateField(default=datetime.date.today(), blank=True)
    receive_stu = models.TextField(default='', blank=True)

    ID = 'id'
    TITLE = 'title'
    TEXT = 'text'
    TEACHER_ID = 'teacher_id'
    SEND_DATE = 'send_date'
    RECEIVE_STU = 'receive_stu'

    FIELD_LIST = [ID, TITLE, TEXT, TEACHER_ID, SEND_DATE,
                  RECEIVE_STU]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Notice._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret


class Group(models.Model):
    name = models.CharField(max_length=500, default='', blank=True)
    vol_list = models.CharField(max_length=500, default='', blank=True)
    stu_list = models.CharField(max_length=500, default='', blank=True)

    ID = 'id'
    NAME = 'name'
    VOL_LIST = 'vol_list'
    STU_LIST = 'stu_list'

    FIELD_LIST = [ID, NAME, VOL_LIST, STU_LIST]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Group._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret


class Timer(models.Model):

    teacher_id = models.IntegerField(default=0, blank=True)
    name = models.CharField(max_length=50, default='', blank=True)
    start_time = models.DateField(default=datetime.date.today, blank=True)
    end_time = models.DateField(default=datetime.date.today, blank=True)
    volunteer_dic = models.CharField(max_length=1000, default='{}', blank=True)

    ID = 'id'

    TEACHER_ID = 'teacher_id'
    NAME = 'name'
    START_TIME = 'start_time'
    END_TIME = 'end_time'
    VOLUNTEER_DIC = 'volunteer_dic'

    FIELD_LIST = [ID, TEACHER_ID, NAME, START_TIME, END_TIME,
                  VOLUNTEER_DIC]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in Timer._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret


class WechatURL(models.Model):

    picture_url = models.CharField(max_length=1000, default='{}', blank=True)
    message_url = models.CharField(max_length=1000, default='{}', blank=True)

    ID = 'id'
    PICTURE_URL = 'picture_url'
    MESSAGE_URL = 'message_url'

    FIELD_LIST = [ID, PICTURE_URL, MESSAGE_URL]

    def __unicode__(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        varList = (vars(item)['column'] for item in WechatURL._meta.get_fields()[1:])
        ret = ''
        for item in varList:
            ret = ret + str(getattr(self, item, 'None')) + ' || '
        return ret

