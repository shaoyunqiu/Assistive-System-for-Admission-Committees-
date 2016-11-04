# coding=utf-8
from django.forms import forms

from models import *
import traceback
from django.core.exceptions import ValidationError


def createNoticebyDict(dict):
    try:
        notice = Notice.objects.model()
    except:
        print "create object fail"
        traceback.print_exc()
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


def setNotice(notice, field, value):
    try:
        setattr(notice, field, value)
        notice.full_clean()
        notice.save()
        return True
    except:
        print "can not saved!!"
        return False


def getNoticebyDict(dic):
    return Notice.objects.filter(**dic)


def getNoticeAllDictByObject(notice):
    dict = {}
    for item in Notice.FIELD_LIST:
        try:
            dict[item] = getattr(notice, item)
        except:
            return None
    return dict

# ------------------------------------------------------------------------------------------------
def createGroupbyDict(dict):
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


def setGroup(group, field, value):
    try:
        setattr(group, field, value)
        group.full_clean()
        group.save()
        return True
    except:
        print "-------------------------------"
        print "can not saved!!"
        return False


def getGroupbyDict(dic):
    if len(dic.keys()) <= 0:
        return Group.objects.all()
    return Group.objects.filter(**dic)


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


































