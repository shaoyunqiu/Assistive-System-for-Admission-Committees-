# coding=utf-8
from django.forms import forms

from models import *
import traceback
from django.core.exceptions import ValidationError


def getAllInPicture():
    return Picture.objects.all()

def deletePictureAll():
    getAllInPicture().delete()


def removePictureID(account):
    getAllInPicture().filter(account=account).delete()


def getPicturebyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个Picture对象
    '''
    dic = {field: argc}
    return Picture.objects.filter(**dic)

def checkField(field):
    '''
    检查传入字段是否存在
    :param field: 字段名
    :return: 是否存在bool
    '''
    if field in Picture.FIELD_LIST:
        return True
    print 'this column not exist'
    return False

def getPictureAll(account):
    '''
    根据account获得学生的所有字段信息,不存在账户名时返回None
    :param account: 学生的账户名
    :return: 学生字段的所有信息
    '''
    acc = Picture.objects.filter(account=account)
    if len(acc) == 0:
        print 'account not exist'
        return None
    if len(acc) > 1:
        print 'warning: account not unique!'
    return acc[0]

def getPicture(account, field):
    '''
    通过account获得学生的field字段的值
    :param account: 学生账户
    :param field: 待查字段
    :return: 待查字段的值
    '''
    if not checkField(field):
        return None
    if not getPictureAll(account):
        return None
    return getattr(getPictureAll(account), field, 'Error')

def setPicture(account, field, value):
    '''
    设置某个账户某个字段的值
    :param account:账户
    :param field:字段
    :return:字段对应的值
    '''
    try:
        if not checkField(field):
            return False
        if field == Picture.ACCOUNT:
            print 'can not modify account'
            return False
        if not getPictureAll(account):
            return False
        pic = getPictureAll(account)
        setattr(pic, field, value)
        pic.full_clean()
        pic.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


def createPicture(account, dict):
    '''
    在数据库中增加一个图片
    :param account:图片名
    :param dict:其余信息的键值对
    :return:是否成功添加
    '''
    if getPictureAll(account):
        print "account existed"
        return False

    try:
        pic = Picture.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False

    try:
        setattr(pic, Picture.ACCOUNT, account)
        for item in dict.keys():
            setattr(pic, item, dict[item])
        print 'full_clean ing...'
        pic.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False

    pic.save()
    print 'successfully create account'
    return True















