# coding=utf-8

from models import *
import traceback
from django.core.exceptions import ValidationError
from my_field import *


def getAllInVolunteer():
    return Volunteer.objects.all()

def getVolunteerAllDictByAccount(account):
    volunteer = getVolunteerAll(account)
    dict = {}
    for item in Volunteer.FIELD_LIST:
        try:
            dict[item] = getattr(volunteer, item)
        except:

            return None

    dict[Volunteer.TYPE] = typeIntToString(dict[Volunteer.TYPE])
    dict[Volunteer.SEX] = sexIntToString(dict[Volunteer.SEX])
    dict[Volunteer.NATION] = {'nation': nationIntToString(dict[Volunteer.NATION]),
                            'nationlist': NATION_LIST}
    dict[Volunteer.PROVINCE] = {'province': provinceIntToString(dict[Volunteer.PROVINCE]),
                              'provincelist': PROVINCE_LIST,

                              }

    major_int_list = dict[Volunteer.MAJOR]
    dict[Volunteer.MAJOR] = []
    for item in major_int_list:
        dict[Volunteer.MAJOR].append({'department': item,
                                  'departmentlist':MAJOR_LIST,})


    dict[Volunteer.ESTIMATE_SCORE] = dict[Volunteer.ESTIMATE_SCORE]
    dict[Volunteer.REAL_SCORE] = dict[Volunteer.REAL_SCORE]
    dict[Volunteer.ADMISSION_STATUS] = admissionStatusIntToString(dict[Volunteer.ADMISSION_STATUS])
    return dict


def deleteVolunteerAll():
    getAllInVolunteer().delete()


def idToAccountVolunteer(id):
    '''

    :param id: string类型的id
    :return: string类型的account
    '''
    try:
        int_id = (int)(id)
    except:
        print 'id is not int'
        return False
    acc = Volunteer.objects.filter(id=int_id)
    if len(acc) == 0:
        print 'id not exist'
        return None
    # if len(acc) > 1:
    #     print 'warning: account not unique!'
    return getattr(acc[0], Volunteer.ACCOUNT, 'Error')

def accountToIDVolunteer(account):
    '''

    :param account: string类型的account
    :return: string类型的id
    '''
    return (str)(getVolunteer(account, 'id'))

def removeVolunteerAccount(_account):
    getAllInVolunteer().filter(account= _account).delete()


def getVolunteerbyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个volunteer对象
    '''
    dic = {field: argc}
    return Volunteer.objects.filter(**dic)


def checkField(field):
    '''
    检查传入字段是否存在
    :param field: 字段名
    :return: 是否存在bool
    '''
    if field in Volunteer.FIELD_LIST:
        return True
    print 'this column not exist'
    return False

def getVolunteerAll(account):
    '''
    根据account获得志愿者的所有字段信息,不存在账户名时返回None
    :param account: 志愿者的账户名
    :return: 志愿者字段的所有信息
    '''
    acc = Volunteer.objects.filter(account=account)
    if len(acc) == 0:
        print 'account not exist'
        return None
    if len(acc) > 1:
        print 'warning: account not unique!'
    return acc[0]


def getVolunteer(account, field):
    '''
    通过account获得学生的field字段的值
    :param account: 学生账户
    :param field: 待查字段
    :return: 待查字段的值
    '''
    if not checkField(field):
        return None
    if not getVolunteerAll(account):
        return None
    return getattr(getVolunteerAll(account), field, 'Error')

def setVolunteer(account, field, value):
    '''
    设置某个账户某个字段的值
    :param account:账户
    :param field:字段
    :return:字段对应的值
    '''
    try:
        if not checkField(field):
            return False
        if field == Volunteer.ACCOUNT:
            print 'can not modify account'
            return False
        if not getVolunteerAll(account):
            return False
        volunteer = getVolunteerAll(account)
        setattr(volunteer, field, value)
        volunteer.full_clean()
        volunteer.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False

def createVolunteer(account, dict):
    '''
    在数据库中增加一个志愿者
    :param account:账户
    :param dict:其余信息的键值对
    :return:是否成功添加
    '''
    if getVolunteerAll(account):
        print "account existed"
        return False

    try:
        volunteer = Volunteer.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False

    try:
        setattr(volunteer, Volunteer.ACCOUNT, account)
        for item in dict.keys():
            setattr(volunteer, item, dict[item])
        print 'full_clean ing...'
        volunteer.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False

    volunteer.save()
    print 'successfully create account'
    return True


def checkVolunteerPassword(_account,_password):
    '''
    检查密码是否正确
    暂时空出
    :param _account: 用户名
    :param _password: 传过来的密码，可能被加密过
    :return:
    '''
    if not getVolunteerAll(_account): #无重复，说明不存在这个用户
        return (False , 'Account does not exist.')
    if _password != getVolunteer(_account, Volunteer.PASSWORD): # 密码不正确
        return (False , 'Password is incorrect')
    return (True, str(getVolunteer(_account, Volunteer.ID)))



