# coding=utf-8

from models import *
import time
import random, string
import traceback
from django.core.exceptions import ValidationError

def getAllInRegisterCode():
    return RegisterCode.objects.all()

def removeRegisterCode(_account):
    getAllInRegisterCode().filter(registerCode=_account).delete()

def deleteRegisterCodeAll():
    getAllInRegisterCode().delete()


def getRegisterCodebydic(dic):
    return RegisterCode.objects.filter(**dic)

def getRegisterCodebyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个对象列表
    '''
    # modified by shaoyunqiu
    if field not in RegisterCode.FIELD_LIST:
        print "illegal field"
        return []
    else:
        dic = {field: argc}
        return RegisterCode.objects.filter(**dic)

def setRegisterCode(code, field, value):
    try:
        if (field in RegisterCode.FIELD_LIST) == False:
            print 'are not'
            return False
        if field == RegisterCode.REGISTER_CODE:
            print 'can not modify code'
            return False
        print 'start set'
        register = getRegisterCodebyField(RegisterCode.REGISTER_CODE, code)
        setattr(register, field, value)
        register.full_clean()
        register.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False

def isExistRegisterCode(code):
    lists = getRegisterCodebyField(RegisterCode.REGISTER_CODE, code)
    if(len(lists) > 0):
        return True
    return False

def tmpcreateNewRegisterCode():
    code = ''
    code = code + time.strftime('%Y', time.localtime(time.time()))
    code = code + str(str(len(getAllInRegisterCode())).zfill(7))
    code = code + random_str(9)
    return code

def createRegisterCode(code):
    obj = RegisterCode.objects.model()
    try:
        setattr(obj, RegisterCode.REGISTER_CODE, code)
        obj.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False
    obj.save()
    return True

def createNewRegisterCode():
    # 产生code直到不重复
    code = tmpcreateNewRegisterCode()
    # while(isExistRegisterCode(code)):
    #     code = tmpcreateNewRegisterCode()

    # 将生成的code加入数据库
    createRegisterCode(code)

    return code

def random_str(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])

