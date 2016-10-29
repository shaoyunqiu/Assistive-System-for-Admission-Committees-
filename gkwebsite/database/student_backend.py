# coding=utf-8

from models import *
import traceback
from django.core.exceptions import ValidationError
from my_field import *
import backend as back


# dic = {'account':'houyf','password':'mima','area':'wuhan','email':'a@qq.com','phone':'11111111','realName':'hyf','volunteerList':['a','b']}

def getAllInStudent():
    return Student.objects.all()


def deleteStudentAll():
    getAllInStudent().delete()


def idToAccountStudent(id):
    '''

    :param id: string类型的id
    :return: string类型的account
    '''
    try:
        int_id = (int)(id)
    except:
        print 'id is not int'
        return False
    acc = Student.objects.filter(id=int_id)
    if len(acc) == 0:
        print 'id not exist'
        return None
    # if len(acc) > 1:
    #     print 'warning: account not unique!'
    return getattr(acc[0], Student.ACCOUNT, 'Error')


def accountToIDStudent(account):
    '''

    :param account: string类型的account
    :return: string类型的id
    '''
    return (str)(getStudent(account, 'id'))


def removeStudentAccount(_account):
    getAllInStudent().filter(account=_account).delete()


def getStudentbyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个student对象
    '''
    dic = {field: argc}
    return Student.objects.filter(**dic)


def checkField(field):
    '''
    检查传入字段是否存在
    :param field: 字段名
    :return: 是否存在bool
    '''
    if field in Student.FIELD_LIST:
        return True
    print 'this column not exist'
    return False


def getStudentAll(account):
    '''
    根据account获得学生的所有字段信息,不存在账户名时返回None
    :param account: 学生的账户名
    :return: 学生字段的所有信息
    '''
    acc = Student.objects.filter(account=account)
    if len(acc) == 0:
        print 'account not exist'
        return None
    if len(acc) > 1:
        print 'warning: account not unique!'
    return acc[0]


def getStudentAllDictByAccount(account):
    student = getStudentAll(account)
    dict = {}
    for item in Student.FIELD_LIST:
        try:
            dict[item] = getattr(student, item)
        except:

            return None

    dict[Student.TYPE] = {
        'type': dict[Student.TYPE],
        'typelist': TYPE_LIST
    }
    dict[Student.SEX] = {
        'sex': dict[Student.SEX],
        'sexlist': SEX_LIST
    }
    dict[Student.NATION] = {
        'nation': dict[Student.NATION],
        'nationlist': NATION_LIST}
    dict[Student.PROVINCE] = {
        'province': dict[Student.PROVINCE],
        'provincelist': PROVINCE_LIST,
    }

    major_int_list = dict[Student.MAJOR]
    for i in range(0, 10):
        major_int_list.append(0)
        dict[Student.TEST_SCORE_LIST].append(0)
        dict[Student.RANK_LIST].append(0)
        dict[Student.SUM_NUMBER_LIST].append(0)
    dict[Volunteer.MAJOR] = []
    for item in major_int_list:
        numitem = (int)(item)
        dict[Volunteer.MAJOR].append({'department': numitem,
                                      'departmentlist': MAJOR_LIST})

    # dict[Student.ADMISSION_STATUS] = {
    #     'admissionstatus': dict[Student.ADMISSION_STATUS],
    #     'admissionstatuslist': ADMISSION_STATUS_LIST
    # }
    return dict


def getStudent(account, field):
    '''
    通过account获得学生的field字段的值
    :param account: 学生账户
    :param field: 待查字段
    :return: 待查字段的值
    '''
    if not checkField(field):
        return None
    if not getStudentAll(account):
        return None
    return getattr(getStudentAll(account), field, 'Error')


def setStudent(account, field, value):
    '''
    设置某个账户某个字段的值
    :param account:账户
    :param field:字段
    :return:字段对应的值
    '''
    try:
        if not checkField(field):
            return False
        if field == Student.ACCOUNT:
            print 'can not modify account'
            return False
        if not getStudentAll(account):
            return False
        student = getStudentAll(account)
        setattr(student, field, value)
        student.full_clean()
        student.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


def createStudent(account, dict):
    '''
    在数据库中增加一个学生
    :param account:账户
    :param dict:其余信息的键值对
    :return:是否成功添加
    '''
    if getStudentAll(account):
        print "account existed"
        return False

    try:
        student = Student.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False

    try:
        setattr(student, Student.ACCOUNT, account)
        for item in dict.keys():
            setattr(student, item, dict[item])
        print 'full_clean ing...'
        student.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False

    student.save()
    print 'successfully create account'
    return True


def checkStudentPassword(_account,_password):
    '''
    检查密码是否正确
    暂时空出
    :param _account: 用户名
    :param _password: 传过来的密码，可能被加密过
    :return:
    '''

    #if _password == hash(getData(_account, 'password')): #哈希
    if not getStudent(_account, 'account'): #无重复，说明不存在这个用户
        print '---------'
        return (False , 'Account does not exist.')
    if _password != getStudent(_account, 'password'):
        print '*********'
        return (False , 'Password is incorrect')
    # 密码不正确
    return (True, str(getStudent(_account,'id')))
    #hash function should be applied here

def getStudentGroupIDListString(student):
    stu_id = 0
    try:
        stu_id = getattr(student, Student.ID)
    except:
        stu_id = 1

    group_all_list = back.getGroupbyDict({})
    id_list = []
    for group in group_all_list:
        stu_list = back.getGroupAllDictByObject(group)[Group.STU_LIST].split('_')
        if str(stu_id) in stu_list:
            id_list.append(str(getattr(group, Group.ID)))
    return ' '.join(id_list)














