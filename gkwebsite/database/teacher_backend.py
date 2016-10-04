# coding=utf-8

from models import *
from django.core.exceptions import ValidationError

def getAll():
    return Teacher.objects.all()

def getObject():
    return Teacher.objects

def deleteAll():
    getAll().delete()

def tupleEqual(a,b):
    '''
    判断俩tuple是否一样
    :param a:
    :param b:
    :return:是否一样
    '''
    if len(a) != len(b):
        return False
    for item in a:
        if item not in b:
            return False
    return True

def createAccount(kwargs):
    '''
    创建新账户
    :param kwargs:应当是包含所有的field信息的字典
    :return:True表示成功添加 False表示添加失败
    '''
    varList = tuple(vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
    # 获取所有Teacher类的field名
    # print tuple(varList)
    # print tuple(kwargs.keys())
    if not tupleEqual(varList,tuple(kwargs.keys())):
        print "parameters passed to createAccount are not correct"
        # print varList
        # print tuple(kwargs.keys())
        return False
    if not checkAccount(kwargs['account']):
        print 'account has been occupied'
        return False
    try:
        teacher = Teacher.objects.create(**kwargs)
    except:
        print "create fail"
        return False
    try:
        teacher.full_clean()
    except ValidationError, e:
        # bug:can not catch exception here
        print e
        return False
    teacher.save()
    return True

def checkAccount(_account):
    '''
    检查用户名是否重复
    :param account:表示用户名的字符串
    :return:True表示无重复 False表示有重复
    '''
    if len(getObject().filter(account = _account)) > 0:
        return False
    #重复
    return True
    #通过检查


def checkPassword(_account,_password):
    '''
    检查密码是否正确
    暂时空出
    :param _account: 用户名
    :param _password: 传过来的密码，可能被加密过
    :return:
    '''
    return True # 先暂时直接通过验证
    #hash function should be applied here

def checkColomn(_colomn):
    '''
    检查是否存在这一个数据列
    :param _colomn:列名称
    :return:是否存在的bool
    '''
    varList = tuple(vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
    return _colomn in varList

def getAccount(_account):
    """
    获取一个账户的信息
    :param _account:老师账户名称
    :return:账户信息
    """
    acc = getObject().filter(account = _account)
    if len(acc) == 0:
        print 'account not exist'
        return None
    if len(acc) > 1:
        print 'warning: account not unique!'
    return acc[0]

def getData(_account,_colomn):
    '''
    获取一个账户某一列信息
    :param _account:账户名
    :param _colomn:列
    :return:信息，可以是字符串、列表等等
    '''
    if not getAccount(_account):
        return None
    if not checkColomn(_colomn):
        print 'this column not exist'
        return None
    return getattr(getAccount(_account), _colomn, 'Error')

def setData(_account,_colomn,_data):
    '''
    设置账户信息
    :param _account:账户名
    :param _colomn:列
    :param _data:要设置成的信息
    :return:是否设置成功
    '''
    if _colomn == 'account':
        print 'can not modify account'
        return False
    if not checkColomn(_colomn):
        print 'this column not exist'
        return False
    teacher = getAccount(_account)
    setattr(teacher, _colomn, _data)
    teacher.full_clean()
    teacher.save()
    return True
