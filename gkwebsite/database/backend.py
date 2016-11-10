# coding=utf-8
from django.forms import forms

from models import *
import traceback
from django.core.exceptions import ValidationError


def createNoticebyDict(dict):
    if 'id' in dict.keys():
        dict.pop('id')

    try:
        notice = Notice.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False
    # modified by shaoyunqiu, cannot set the id and chedk field
    if Notice.ID in dict.keys():
        print "cannot set the id, cannot create"
        return False
    for field in dict.keys():
        if field not in Notice.FIELD_LIST:
            print "illegal, field"
            return False

    try:
        for item in dict.keys():
            setattr(notice, item, dict[item])
        print 'full_clean ing...'
        notice.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False
    notice.save()
    print 'successfully create account'
    return True


# modified by shaoyunqiu, cannot set the id, and check the field is legal.
def setNotice(notice, field, value):
    if field == Notice.ID :
        print "cannot set the id, fail"
        return False
    if field not in Notice.FIELD_LIST:
        print "illegal field"
    try:
        setattr(notice, field, value)
        notice.full_clean()
        notice.save()
        return True
    except:
        print "can not saved!!"
        return False

# modified by shaoyunqiu, check the field
def getNoticebyDict(dic):
    for field in dic.keys():
        if field not in Notice.FIELD_LIST:
            print "illegal field"
            return []
    return Notice.objects.filter(**dic)


def getNoticeAllDictByObject(notice):
    dict = {}
    for item in Notice.FIELD_LIST:
        try:
            dict[item] = getattr(notice, item)
        except:
            # print 'item ',item
            # print getattr(notice, item)
            return None
    return dict

# ------------------------------------------------------------------------------------------------
def createGroupbyDict(dict):
    # modified by shaoyunqiu to forbiden set the id and illegal field
    '''if Group.ID in dict.keys():
        print "cannot set the id, failed"
        return False'''
    for field in dict.keys():
        if field not in Group.FIELD_LIST:
            print "illegal field, failed"
            return False
    if 'id' in dict.keys():
        dict.pop('id')

    try:
        group = Group.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False
    try:
        for item in dict.keys():
            setattr(group, item, dict[item])
        print 'full_clean ing...'
        group.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False
    group.save()
    print 'successfully create account'
    return True

# modified by shaoyunqiu, cannot set the id, and check the field is legal.
def setGroup(group, field, value):
    if field == Group.ID :
        print "cannot set the id, fail"
        return False
    if field not in Group.FIELD_LIST:
        print "illegal field"
    try:
        setattr(group, field, value)
        group.full_clean()
        group.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


# modified by shaoyunqiu, check the field, the first check is no need.
def getGroupbyDict(dic):
    '''if len(dic.keys()) <= 0:
        return Group.objects.all()'''
    try:
        for field in dic.keys():
            if field not in Group.FIELD_LIST:
                print "illegal key"
                return []
    except:
        print "dict error"
        return []
    try:
        ans = Group.objects.filter(**dic)
        return ans
    except:
        print "failed"
        return []


def getGroupAllDictByObject(group):
    dict = {}
    for item in Group.FIELD_LIST:
        try:
            # print 'ri ', getattr(group, item)
            dict[item] = getattr(group, item)
        except:
            return None
    return dict


# ------------------------------------------------------------------------------------------------
def createTimerbyDict(dict):
    # modified by shaoyunqiu, cannot set id and illegal field
    '''if Timer.ID in dict.keys():
        print "cannot set the id, failed"
        return False'''
    for field in dict.keys():
        if field not in Timer.FIELD_LIST:
            print "illegal field, failed"
            return False
    if 'id' in dict.keys():
        dict.pop('id')
    try:
        timer = Timer.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False
    try:
        for item in dict.keys():
            setattr(timer, item, dict[item])
        print 'full_clean ing...'
        timer.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False
    timer.save()
    print 'successfully create account'
    return True


def setTimer(timer, field, value):
    if field == 'id':
        return False
    try:
        setattr(timer, field, value)
        timer.full_clean()
        timer.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


def getTimerbyDict(dic):
    return Timer.objects.filter(**dic)


def getTimerAllDictByObject(timer):
    dict = {}
    for item in Timer.FIELD_LIST:
        try:
            dict[item] = getattr(timer, item)
        except:
            return None
    if dict[Timer.VOLUNTEER_DIC].strip() == '':
        dict[Timer.VOLUNTEER_DIC] = '{}'
    try:
        dict[Timer.VOLUNTEER_DIC] = eval(dict[Timer.VOLUNTEER_DIC])
    except:
        print 'Can not change to dict'
        dict[Timer.VOLUNTEER_DIC] = {}
    return dict

def removeTimerByDic(dic):
    Timer.objects.all().filter(**dic).delete()



# ------------------------------------------------------------------------------------------------
def createWechatURLbyDict(dict):
    if 'id' in dict.keys():
        dict.pop('id')
    try:
        wechatURL = WechatURL.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
        return False
    try:
        for item in dict.keys():
            setattr(wechatURL, item, dict[item])
        print 'full_clean ing...'
        wechatURL.full_clean()
    except ValidationError:
        print 'validation fail...'
        traceback.print_exc()
        return False
    wechatURL.save()
    print 'successfully create account'
    return True


def setWechatURL(wechatURL, field, value):
    if field == 'id':
        return False
    try:
        setattr(wechatURL, field, value)
        wechatURL.full_clean()
        wechatURL.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


def getWechatURLbyDict(dic):
    return WechatURL.objects.filter(**dic)


def getWechatURLAllDictByObject(wechatURL):
    dict = {}
    for item in WechatURL.FIELD_LIST:
        try:
            dict[item] = getattr(wechatURL, item)
        except:
            return None
    return dict


def removeWechatURLByDic(dic):
    WechatURL.objects.all().filter(**dic).delete()


def date_start_to_end(start, end):
    if start > end:
        print 'time error'
        return None
    date_list = []
    while True:
        date_list.append(start.strftime("%Y/%m/%d"))
        start = start + datetime.timedelta(days=1)
        if start > end:
            break
    valid_list = []
    for item in date_list:
        valid_list.append('0')
    return (date_list, valid_list)


def check_volunteerID_date(timer_id, vol_id, date):
    timer = getTimerbyDict({Timer.ID:int(timer_id)})[0]
    info_dic = getTimerAllDictByObject(timer)
    vol_dic = info_dic[Timer.VOLUNTEER_DIC]
    if date < info_dic[Timer.START_TIME] or date > info_dic[Timer.END_TIME]:
        return False
    delta_day = int((date - info_dic[Timer.START_TIME]).days)
    if str(vol_id) in vol_dic.keys():
        if vol_dic[str(vol_id)][delta_day] == '1':
            return True
    return False


def getLastOneWechatURL():
    all_wechat_url = getWechatURLbyDict({})
    if len(all_wechat_url) <= 0:
        return None
    info_dic = getWechatURLAllDictByObject(all_wechat_url[-1])
    return info_dic


def getLastTenWechatURL():
    all_wechat_url = getWechatURLbyDict({})
    end = len(all_wechat_url)
    start = len(all_wechat_url) - 10
    ret_list = []
    for i in range(start, end):
        if i >= 0 and i < len(all_wechat_url):
            info_dic = getWechatURLAllDictByObject(all_wechat_url[i])
            ret_list.append(info_dic)
    return ret_list





































