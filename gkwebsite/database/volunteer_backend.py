# coding=utf-8

from models import *
import traceback
from django.core.exceptions import ValidationError
from my_field import *
import backend as back

MIN_LEN_FOR_LIST = 10

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

    dict[Volunteer.TYPE] = {
        'type': dict[Volunteer.TYPE],
        'typelist': TYPE_LIST
    }
    dict[Volunteer.SEX] = {
        'sex': dict[Volunteer.SEX],
        'sexlist': SEX_LIST
    }
    dict[Volunteer.NATION] = {
        'nation': dict[Volunteer.NATION],
        'nationlist': NATION_LIST}
    dict[Volunteer.PROVINCE] = {
        'province': dict[Volunteer.PROVINCE],
        'provincelist': PROVINCE_LIST,
    }
    # dict[Volunteer.ADMISSION_STATUS] = {
    #     'admissionstatus': dict[Volunteer.ADMISSION_STATUS],
    #     'admissionstatuslist': ADMISSION_STATUS_LIST
    # }

    major_int_list = dict[Volunteer.MAJOR]
    for i in range(0, MIN_LEN_FOR_LIST):
        major_int_list.append(0)
        dict[Volunteer.TEST_SCORE_LIST].append(0)
        dict[Volunteer.RANK_LIST].append(0)
        dict[Volunteer.SUM_NUMBER_LIST].append(0)

    dict[Volunteer.MAJOR] = []
    for item in major_int_list:
        numitem = (int)(item)
        dict[Volunteer.MAJOR].append({'department': numitem,
                                      'departmentlist': MAJOR_LIST})



    return dict



def deleteVolunteerAll():
    getAllInVolunteer().delete()


def is_have_permission(_id):
    if type(_id) == str:
        _id = int(_id)
    account = idToAccountVolunteer(_id)
    ret = getVolunteer(account, Volunteer.QUANXIAN)
    if ret == 1:
        return True
    else:
        return False


def idToAccountVolunteer(id):
    '''

    :param id: string类型的id
    :return: string类型的account
    '''
    try:
        int_id = (int)(id)
    except:
        # print 'id is not int'
        return False
    acc = Volunteer.objects.filter(id=int_id)
    if len(acc) == 0:
        # print 'id not exist'
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

    vol_id = str(accountToIDVolunteer(_account))
    group_list = back.getGroupbyDict({})
    for group in group_list:
        vol_list = getattr(group, Group.VOL_LIST).split('_')
        if vol_id in vol_list:
            vol_list.remove(vol_id)
        if '' in vol_list:
            vol_list.remove('')
        back.setGroup(group, Group.VOL_LIST, '_'.join(vol_list))

    timer_list = back.getTimerbyDict({})
    for timer in timer_list:
        timer_dic = eval(getattr(timer, Timer.VOLUNTEER_DIC, '{}'))
        if vol_id in timer_dic.keys():
            timer_dic.pop(vol_id)
        back.setTimer(timer, Timer.VOLUNTEER_DIC, timer_dic)
    getAllInVolunteer().filter(account=_account).delete()

def getVolunteerbyField(field, argc):
    '''
    :param field:待查询的字段
    :param argc:字段的值
    :return:返回一个volunteer对象
    '''

    #shaoyunqiu need to checkfield
    # checked by lihy 2016/11/07
    if (checkField(field) == True):
        dic = {field: argc}
        return Volunteer.objects.filter(**dic)
    else:
        # print "field is not exist"
        return []


def checkField(field):
    '''
    检查传入字段是否存在
    :param field: 字段名
    :return: 是否存在bool
    '''
    if field in Volunteer.FIELD_LIST:
        return True
    # print 'this column not exist'
    return False

def getVolunteerAll(account):
    '''
    根据account获得志愿者的所有字段信息,不存在账户名时返回None
    :param account: 志愿者的账户名
    :return: 志愿者字段的所有信息
    '''
    acc = Volunteer.objects.filter(account=account)
    if len(acc) == 0:
        # print 'account not exist'
        return None
    if len(acc) > 1:
        # print 'warning: account not unique!'
        pass
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
    if field == 'id':
        return False
    try:
        if not checkField(field):
            return False
        if field == Volunteer.ACCOUNT:
            # print 'can not modify account'
            return False
        if not getVolunteerAll(account):
            return False
        volunteer = getVolunteerAll(account)
        setattr(volunteer, field, value)
        volunteer.full_clean()
        volunteer.save()
        return True
    except:
        # print "-------------------------------"
        # print "can not saved!!"
        return False

def createVolunteer(account, dict):
    '''
    在数据库中增加一个志愿者
    :param account:账户
    :param dict:其余信息的键值对
    :return:是否成功添加
    '''
    if 'id' in dict.keys():
        dict.pop('id')

    if getVolunteerAll(account):
        # print "account existed"
        return False

    try:
        volunteer = Volunteer.objects.model()
    except:
        # print "create object fail"
        traceback.print_exc()
        return False

    try:
        setattr(volunteer, Volunteer.ACCOUNT, account)
        for item in dict.keys():
            setattr(volunteer, item, dict[item])
        # print 'full_clean ing...'
        volunteer.full_clean()
    except ValidationError:
        # print 'validation fail...'
        traceback.print_exc()
        return False

    volunteer.save()
    # print 'successfully create account'
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


def getVolunteerGroupIDListString(volunteer):
    try:
        vol_id = getattr(volunteer, Volunteer.ID)
    except:
        vol_id = 1

    group_all_list = back.getGroupbyDict({})
    id_list = []
    for group in group_all_list:
        vol_list = back.getGroupAllDictByObject(group)[Group.VOL_LIST].split('_')
        if str(vol_id) in vol_list:
            id_list.append(str(getattr(group, Group.ID)))
    return ' '.join(id_list)


def setVolunteerGroupbyList(volunteer, id_list):
    try:
        vol_id = str(getattr(volunteer, Volunteer.ID))
    except:
        vol_id = str(1)

    group_all_list = back.getGroupbyDict({})
    for group in group_all_list:
        vol_list = back.getGroupAllDictByObject(group)[Group.VOL_LIST].split('_')
        if vol_id in vol_list:
            vol_list.remove(vol_id)
        if '' in vol_list:
            vol_list.remove('')
        vol_string = '_'.join(vol_list)
        back.setGroup(group, Group.VOL_LIST, vol_string)

    for new_id in id_list:
        new_id = str(new_id)
        if len(back.getGroupbyDict({Group.ID: new_id})) <= 0:
            continue
        group = back.getGroupbyDict({Group.ID: new_id})[0]
        vol_list = back.getGroupAllDictByObject(group)[Group.VOL_LIST].split('_')
        if '' in vol_list:
            vol_list.remove('')
        if vol_id in vol_list:
            print 'Big bug!'
        else:
            vol_list.append(vol_id)
        back.setGroup(group, Group.VOL_LIST, '_'.join(vol_list))
    return True

def get_can_see_students(vol_id):
    all_group = back.getGroupbyDict({})
    stu_id_list = []
    for group in all_group:
        vol_list = getattr(group, Group.VOL_LIST).split('_')
        if '' in vol_list:
            vol_list.remove('')
        if str(vol_id) in vol_list:
            tmp_list = getattr(group, Group.STU_LIST).split('_')
            stu_id_list = stu_id_list + tmp_list

    ret = []
    for _id in stu_id_list:
        if _id != '':
            try:
                ret.append(int(_id))
            except:
                pass
    return ret




