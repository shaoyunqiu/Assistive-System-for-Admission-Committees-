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
        # print "illegal field"
        return []
    else:
        dic = {field: argc}
        return RegisterCode.objects.filter(**dic)

def setRegisterCode(code, field, value):
    try:
        if (field in RegisterCode.FIELD_LIST) == False:
            # print 'are not'
            return False
        if field == RegisterCode.REGISTER_CODE:
            # print 'can not modify code'
            return False
        # print 'start set'
        # modified by shaoyunqiu. register need to be an object
        register = getRegisterCodebyField(RegisterCode.REGISTER_CODE, code)[0]
        setattr(register, field, value)
        register.full_clean()
        register.save()
        return True
    except:
        # print "-------------------------------"
        # print "can not saved!!"
        return False

def isExistRegisterCode(code):
    lists = getRegisterCodebyField(RegisterCode.REGISTER_CODE, code)
    if(len(lists) > 0):
        return True
    return False

def swap_str(str, i,j):
    ci = str[i]
    cj = str[j]
    return str[:i-1] + cj + str[i+1:j-1] + ci + str[j-1:]


def tmpcreateNewRegisterCode():
    code = ''
    code = code + time.strftime('%Y', time.localtime(time.time()))
    code = code + 'GKZS'
    code = code + str(str(len(getAllInRegisterCode()) + 139246).zfill(7))
    code = code + random_str(5)

    code = code[:9] + (code[10] + 'B') + code[11:]
    code = code[:11] + (code[12] + 'C') + code[13:]
    code = swap_str(code, 10, 17)

    ret = code[:-16]+ '-' +code[-16:-12] + '-' + code[-12:-8] + '-' + code[-8:-4] + '-' + code[-4:]
    ret = ret.upper()
    ret = ret.replace('O','0')

    return ret

def createRegisterCode(code):
    obj = RegisterCode.objects.model()
    # modified by shaoyunqiu, registercode need to be unique
    if isExistRegisterCode(code):
        # print "the registercode already exist, can not save"
        return False

    try:
        setattr(obj, RegisterCode.REGISTER_CODE, code)
        obj.full_clean()
    except ValidationError:
        # print 'validation fail...'
        traceback.print_exc()
        return False
    obj.save()
    return True

def createNewRegisterCode():
    # 产生code直到不重复
    code = tmpcreateNewRegisterCode()
    #while(isExistRegisterCode(code)):
    #     code = tmpcreateNewRegisterCode()

    # 将生成的code加入数据库
    # modified by shaoyunqiu, to confirm the registercode have been add to database successfully
    # checked by lihy
    while(True):
        flag = createRegisterCode(code)
        if flag == True:
            break
        else:
            # print "try again"
            code = tmpcreateNewRegisterCode()
    return code


def random_str(randomlength=8):
    # modified by shaoyunqiu
    if randomlength < 1 or randomlength > 255 :
        randomlength = 8
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])

