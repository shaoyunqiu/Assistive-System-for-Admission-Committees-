# coding=utf-8
from django.forms import forms

from models import *
import traceback
from django.core.exceptions import ValidationError


def getAllInPicture():
    return Picture.objects.all()

def deletePictureAll():
    getAllInPicture().delete()

# shaoyunqiu
'''
def removePictureIDByDic(dic):
    getAllInPicture().filter(**dic).delete()
'''
# create and rewrite by shaoyunqiu
def removePictureIDByDic(dic):
    for key in dic.keys():
        if key not in Picture.FIELD_LIST:
            # print "illegal key, can't remove"
            return False
    toremove = Picture.objects.filter(**dic)
    if len(toremove) == 0:
        # print "cant not find the picture"
        return False
    else:
        try:
            toremove.delete()
            return True
        except:
            # print "cannot remove"
            return False

def getPictureAllDictByObject(picture):
    dict = {}
    for item in Picture.FIELD_LIST:
        try:
            dict[item] = getattr(picture, item)
            # print '******'
        except:
            # print '----', item
            return None
    return dict

# modified by shaoyunqiu
def getPicturebyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个Picture对象
    '''
    if field not in Picture.FIELD_LIST:
        return []
    else:
        dic = {field: argc}
        return Picture.objects.filter(**dic)


# modified by shaoyunqiu
def getPicturebyDict(dic):
    '''
    如果在这里有关于isTitle的字段就返回所有isTitile==1的
    :param dic:
    :return:
    '''
    # if Picture.IS_TITLE not in dic.keys():
    #     dic[Picture.IS_TITLE] = 0
    for key in dic.keys():
        if key not in Picture.FIELD_LIST:
            # print "illegal key, cannot find"
            return []
    return Picture.objects.filter(**dic)


def createPicturebyDict(dict):

    # if getPicturebyDict(dict):
    #     print "account existed"
    #     return False
    # modify by shaoyunqiu
    if Picture.ID in dict.keys():
        # print "cannot set id, failed"
        return False
    for field in dict.keys():
        if field not in Picture.FIELD_LIST:
            # print "illegal field, failed"
            return False
    try:
        pic = Picture.objects.model()
    except:
        # print "create object fail"
        traceback.print_exc()
        return False
    try:
        for item in dict.keys():
            setattr(pic, item, dict[item])
        # print 'full_clean ing...'
        pic.full_clean()
    except:
        # print 'validation fail...'
        traceback.print_exc()
        return False

    pic.save()
    # print 'successfully create account'
    return True

# modified by shaoyunqiu
def setPicture(picture, field, value):
    '''
    设置某个账户某个字段的值
    :param account:账户
    :param field:字段
    :return:字段对应的值
    '''
    if field == Picture.ID :
        # print "cannot change the id"
        return False
    if field not in Picture.FIELD_LIST:
        # print "illegal field, cannot set"
        return False
    try:
        setattr(picture, field, value)
        picture.full_clean()
        picture.save()
        # print "before return true"
        return True
    except:
        # print "---------------------"
        # print "can not saved!!"
        return False














