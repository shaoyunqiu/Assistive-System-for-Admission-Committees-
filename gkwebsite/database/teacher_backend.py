# coding=utf-8

from models import *

def getAll():
    return Teacher.objects.all()

def getObject():
    return Teacher.objects

def deleteAll():
    getAll().delete()

def createAccount(kwargs):
    '''
    创建新账户
    :param kwargs:
    :return:
    '''
    varList = tuple(vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
    #获取所有Teacher类的field名
    #print tuple(varList)
    print tuple(kwargs.keys())
    if cmp(varList,tuple(kwargs.keys())):
        print "parameters passed to createAccount are not correct"
        return False
    if not checkAccount(kwargs['account']):
        print 'account has been occupied'
        return False
    try:
        teacher = Teacher.objects.create(**kwargs)
    except:
        print "create fail"
        return False
    teacher.full_clean()
    teacher.save()
    return True

def checkAccount(account):
    '''
    检查用户名是否重复
    :param account:
    :return:
    '''
    if len(getObject().filter(account = account)) > 0:
        return False
    #重复
    return True
    #通过检查


def checkPassword():
    pass
    #hash function should be applied here

