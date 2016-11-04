# coding=utf-8
from django.forms import forms

from models import *
import traceback
from django.core.exceptions import ValidationError


def getAllInPicture():
    return Picture.objects.all()

def deletePictureAll():
    getAllInPicture().delete()


def removePictureIDByDic(dic):
    getAllInPicture().filter(**dic).delete()


def getPictureAllDictByObject(picture):
    dict = {}
    for item in Picture.FIELD_LIST:
        try:
            dict[item] = getattr(picture, item)
            # print '******'
        except:
            print '----', item
            return None
    return dict

def getPicturebyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个Picture对象
    '''
    dic = {field: argc}
    return Picture.objects.filter(**dic)


def getPicturebyDict(dic):
    '''
    如果在这里有关于isTitle的字段就返回所有isTitile==1的
    :param dic:
    :return:
    '''
    # if Picture.IS_TITLE not in dic.keys():
    #     dic[Picture.IS_TITLE] = 0

    return Picture.objects.filter(**dic)


def createPicturebyDict(dict):

    # if getPicturebyDict(dict):
    #     print "account existed"
    #     return False
    try:
        pic = Picture.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False
    try:
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


def setPicture(picture, field, value):
    '''
    设置某个账户某个字段的值
    :param account:账户
    :param field:字段
    :return:字段对应的值
    '''
    try:
        setattr(picture, field, value)
        picture.full_clean()
        picture.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False














