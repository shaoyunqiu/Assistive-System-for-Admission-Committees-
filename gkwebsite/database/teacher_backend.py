# coding=utf-8

from models import *
import traceback
from django.core.exceptions import ValidationError
# dic = {'account':'houyf','password':'mima','area':'wuhan','email':'a@qq.com','phone':'11111111','realName':'hyf','volunteerList':['a','b']}

def getAllInTeacher():
    return Teacher.objects.all()

def getTeacherObject():
    return Teacher.objects

def deleteTeacherAll():
    getAllInTeacher().delete()

def getAllFieldInTeacher():
    return Teacher._meta.get_fields()

def idToAccountTeacher(id):
    '''
    :param id: string类型的id
    :return: string类型的account
    '''
    try:
        int_id = (int)(id)
    except:
        print 'id is not int'
        return False
    acc = Teacher.objects.filter(id=int_id)
    if len(acc) == 0:
        print 'id not exist'
        return None
    # if len(acc) > 1:
    #     print 'warning: account not unique!'
    return getattr(acc[0], 'account', 'Error')

def createTeacher(kwargs):
    '''
    创建新账户
    :param kwargs:应当是包含所有的field信息的字典
    :return:True表示成功添加 False表示添加失败
    '''
    #varList = tuple(vars(item)['column'] for item in Teacher._meta.get_fields()[1:])
    # 获取所有Teacher类的field名
    # shaoyunqiu
    # checked by lihy 2016/11/7
    if 'account' not in kwargs.keys():
        print 'account is required'
        return False
    if kwargs.has_key(Teacher.ID):
        print "cannot set the id"
        return False

    if not checkTeacherAccount(kwargs['account']):
        print 'account has been occupied'
        return False
    try:
        teacher = Teacher.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False
    try:
        for item in kwargs.keys():
            if hasattr(teacher, item):
                setattr(teacher, item, kwargs[item])
        print 'full_clean ing...'
        teacher.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False
    teacher.save()
    print 'successfully create account'
    return True

def checkTeacherAccount(_account):
    '''
    检查用户名是否重复
    :param account:表示用户名的字符串
    :return:True表示无重复 False表示有重复
    '''
    if len(getTeacherObject().filter(account = _account)) == 0:
        return True
    # 通过检查
    return False
    # 重复


def checkTeacherPassword(_account,_password):
    '''
    检查密码是否正确
    暂时空出
    :param _account: 用户名
    :param _password: 传过来的密码，可能被加密过
    :return:
    '''

    #if _password == hash(getData(_account, 'password')): #哈希
    if checkTeacherAccount(_account): #无重复，说明不存在这个用户
        return (False , 'Account does not exist.')
    if _password != getTeacher(_account, 'password'):
        return (False , 'Password is incorrect')
    # 密码不正确
    return (True, str(getTeacher(_account,'id')))
    #hash function should be applied here

def checkTeacherField(_colomn):
    '''
    检查是否存在这一个数据列
    :param _colomn:列名称
    :return:是否存在的bool
    '''
    varList = tuple(vars(item)['column'] for item in Teacher._meta.get_fields())
    return _colomn in varList

def getTeacherAll(_account):
    """
    获取一个账户的信息
    :param _account:老师账户名称
    :return:账户信息
    """
    acc = getTeacherObject().filter(account = _account)
    if len(acc) == 0:
        print 'account not exist'
        return None
    if len(acc) > 1:
        print 'warning: account not unique!'
    return acc[0]

def getTeacher(_account,_colomn):
    '''
    获取一个账户某一列信息
    :param _account:账户名
    :param _colomn:列
    :return:信息，可以是字符串、列表等等
    '''
    if not getTeacherAll(_account):
        #不存在账户
        return None
    if not checkTeacherField(_colomn):
        print 'this column not exist'
        return None
    return getattr(getTeacherAll(_account), _colomn, 'Error')

def setTeacher(_account,_colomn,_data):
    '''
    设置账户信息
    :param _account:账户名
    :param _colomn:列
    :param _data:要设置成的信息
    :return:是否设置成功
    '''
    try:
        if _colomn == 'account':
            print 'can not modify account'
            return False
        if not checkTeacherField(_colomn):
            print 'this column not exist'
            return False
        teacher = getTeacherAll(_account)
        setattr(teacher, _colomn, _data)
        teacher.full_clean()
        teacher.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


