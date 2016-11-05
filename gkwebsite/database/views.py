# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from models import *
import student_backend as stu
import teacher_backend as tch
import volunteer_backend as vol
import register_backend as reg
import image_backend as pic
from my_field import *
import backend as back

from teacher.views import generateTimerXLS


# Create your views here.


def search_student_by_name(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        name = request.POST.get('name')
        stu_list = stu.getStudentbyField(Student.REAL_NAME, name)
        for item in stu_list:
            account = getattr(item, Student.ACCOUNT)
            stu_dic = stu.getStudentAllDictByAccount(account)
            dic = {'id': stu_dic[Student.ID],
                   'name': stu_dic[Student.REAL_NAME],
                   'gender': stu_dic[Student.SEX]['sexlist'][stu_dic[Student.SEX]['sex']],
                   'source': stu_dic[Student.PROVINCE]['provincelist'][stu_dic[Student.PROVINCE]['province']],
                   'school': stu_dic[Student.SCHOOL],
                   'id_card': stu_dic[Student.ID_NUMBER],
                   }
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def remove_student_by_id(request):
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = stu.idToAccountStudent(id)
        stu.removeStudentAccount(account)
        return JsonResponse({})  # return nothing
    else:
        return HttpResponse('Access denied.')


def student_list_all(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        stu_list = stu.getAllInStudent()
        # search for students in database
        for item in stu_list:
            account = getattr(item, Student.ACCOUNT)
            stu_dic = stu.getStudentAllDictByAccount(account)
            dic = {'id': stu_dic[Student.ID],
                   'name': stu_dic[Student.REAL_NAME],
                   'gender': stu_dic[Student.SEX]['sexlist'][stu_dic[Student.SEX]['sex']],
                   'source': stu_dic[Student.PROVINCE]['provincelist'][stu_dic[Student.PROVINCE]['province']],
                   'school': stu_dic[Student.SCHOOL],
                   'id_card': stu_dic[Student.ID_NUMBER],
                   }
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def get_teacher_name_by_id(request):
    '''
    通过id获得老师的名称
    :param request:
    :return:
    '''
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = tch.idToAccountTeacher(id)
        t = {'name': tch.getTeacher(account, 'realName')}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def get_volunteer_name_by_id(request):
    # by dqn14 Oct 19, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = vol.idToAccountVolunteer(id)
        t = {'name': vol.getVolunteer(account, 'realName')}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def get_student_name_by_id(request):
    # by dqn14 Nov 3, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = int(request.POST.get('id'))
        account = stu.idToAccountStudent(id)
        name = stu.getStudent(account, Student.REAL_NAME)
        t = {'name': name}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')

def search_volunteer_by_name(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        name = request.POST.get('name')
        volunteer_list = vol.getVolunteerbyField(Volunteer.REAL_NAME, name)
        for item in volunteer_list:
            account = getattr(item, Volunteer.ACCOUNT)
            vol_dic = vol.getVolunteerAllDictByAccount(account)
            dic = {'id': vol_dic[Volunteer.ID],
                   'name': vol_dic[Volunteer.REAL_NAME],
                   'department': vol_dic[Volunteer.MAJOR][0]['departmentlist'][vol_dic[Volunteer.MAJOR][0]['department']],
                   'class': vol_dic[Volunteer.CLASSROOM],
                   'student_id': vol_dic[Volunteer.STUDENT_ID],
                   }
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def remove_volunteer_by_id(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        vol.removeVolunteerAccount(vol.idToAccountVolunteer(id))
        return JsonResponse({})  # return nothing
    else:
        return HttpResponse('Access denied.')


def volunteer_list_all(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        vol_list = vol.getAllInVolunteer()
        # print vol_list, '***********'
        for item in vol_list:
            account = getattr(item, Volunteer.ACCOUNT)
            vol_dic = vol.getVolunteerAllDictByAccount(account)
            dic = {'id': vol_dic[Volunteer.ID],
                   'name': vol_dic[Volunteer.REAL_NAME],
                   'department': vol_dic[Volunteer.MAJOR][0]['departmentlist'][vol_dic[Volunteer.MAJOR][0]['department']],
                   'class': vol_dic[Volunteer.CLASSROOM],
                   'student_id': vol_dic[Volunteer.STUDENT_ID],
                   }
            # 没注册的志愿者不显示出来
            if dic['name'] != '':
                t.append(dic)
        # print t
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def add_student(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        num = request.POST.get('num')
        num = (int)(num)
        t = []
        codelist = []
        for i in range(0, num):
            code = str(reg.createNewRegisterCode())
            c = {'code': code}
            t.append(c)
            codelist.append(code)
        id = (str)(request.session['teacher_id'])
        generateExcel(request, id, '', '', 'sheet1', [codelist], [u'注册码'])
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def add_volunteer(request):
    # by dqn14 Oct 17, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dic = {Volunteer.PASSWORD: password}
        if vol.createVolunteer(username, dic):
            flag = 'true'
        else:
            flag = 'false'
        print '-------' + username + ' ' + password + ' ' + str(flag)
        return JsonResponse({'success': flag, 'username': username})
    else:
        return HttpResponse('Access denied.')


def export_registration_code(request):
    # by dqn14 Oct 22, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        teacher = request.POST.get('id')
        length = request.POST.get('length')
        filename = "%s_teacher.xls" % teacher
        t = {'filename': filename}
        print 'file xls ' + filename
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def get_teacher_alert_by_id(request):
    # by dqn14 Oct 22, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = {}
        t["message"] = "15"
        t["score"] = get_num_teacher_shenhe_estimate()
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')

def get_num_teacher_shenhe_estimate():
    '''
    获得老师应该审核的学生估分数目
    :return:
    '''
    student_list = stu.getAllInStudent()
    num = 0
    for student in student_list:
        account = getattr(student, Student.ACCOUNT)
        try:
            esti_dic = eval(stu.getStudent(account, Student.ESTIMATE_SCORE))
        except:
            esti_dic = {}
        for key in esti_dic.keys():
            info_dic = esti_dic[key]
            if 'shenhe' not in info_dic.keys():
                num = num + 1

    return num



def test_list_all(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        pic_list = pic.getPicturebyDict({Picture.IS_TITLE: 1})
        for item in pic_list:
            c = {}
            dic = pic.getPictureAllDictByObject(item)
            c['id'] = '%s_%s_%s' % (str(YEAR_LIST[dic[Picture.YEAR]]),
                                    SHITI_LIST[dic[Picture.PROVINCE]],
                                    SUBJECT_LIST[dic[Picture.SUBJECT]])
            c["year"] = str(YEAR_LIST[dic[Picture.YEAR]])
            c["place"] = SHITI_LIST[dic[Picture.PROVINCE]]
            c["subject"] = SUBJECT_LIST[dic[Picture.SUBJECT]]


            if dic[Picture.IS_DELEVERED] == 1:
                c["released"] = "Y"
            else:
                c["released"] = "N"
            t.append(c)
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def release_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        print 'fabu ',id
        list = id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic_list = pic.getPicturebyDict(dic)
        t = {}
        for item in pic_list:
            flag = pic.setPicture(item, Picture.IS_DELEVERED, 1)
            if flag is False:
                t['success'] = 'N'
                t['message'] = '管理员正忙'
                return JsonResponse(t)

        t['success'] = 'Y'
        t['message'] = 'ok'
        print 'ttt ', t
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def withdraw_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        print 'chehui ', id
        list = id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)

        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic_list = pic.getPicturebyDict(dic)
        t = {}
        for item in pic_list:
            flag = pic.setPicture(item, Picture.IS_DELEVERED, 0)
            if flag == False:
                t['success'] = 'N'
                t['message'] = '管理员正忙'
                return JsonResponse(t)

        t['success'] = 'Y'
        t['message'] = 'ok'



        student_list = stu.getAllInStudent()
        for student in student_list:
            account = getattr(student, Student.ACCOUNT)
            estimate = eval(getattr(student, Student.ESTIMATE_SCORE))
            if id in estimate.keys():
                estimate.pop(id)
            stu.setStudent(account, Student.ESTIMATE_SCORE, estimate)


        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def remove_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        list = id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic.removePictureIDByDic(dic)
        t={}
        t['success'] = 'Y'
        t['message'] = 'ok'


        student_list = stu.getAllInStudent()
        for student in student_list:
            account = getattr(student, Student.ACCOUNT)
            estimate = eval(getattr(student, Student.ESTIMATE_SCORE))
            if id in estimate.keys():
                estimate.pop(id)
            stu.setStudent(account, Student.ESTIMATE_SCORE, estimate)


        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def add_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        year = request.POST.get('year')
        place = request.POST.get('place')
        subject = request.POST.get('subject')
        t = {}
        # print year, place, subject
        if year.strip() == '0' or place.strip() == '0' or subject.strip() == '0':
            t['success'] = 'N'
            t['message'] = u'请补全信息'
            return JsonResponse(t)
        if year.strip() == '' or place.strip() == '' or subject.strip() == '':
            t['success'] = 'N'
            t['message'] = u'请补全信息'
            return JsonResponse(t)
        dict = {
            Picture.YEAR : int(year),
            Picture.PROVINCE: int(place),
            Picture.SUBJECT: int(subject),
            Picture.IS_TITLE: 1,
        }

        if pic.getPicturebyDict(dict):
            t['success'] = 'N'
            t['message'] = u'创建失败，试卷已经存在'
            return JsonResponse(t)



        flag = pic.createPicturebyDict(dict)

        if flag:
            t['success'] = 'Y'
            t['message'] = 'ok'
        else:
            t['success'] = 'N'
            t['message'] = '管理员正忙'

        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def get_test_yearlist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        t.append({'num': '', 'str': ''})
        year_len = len(YEAR_LIST)
        for i in range(1, year_len):
            t.append({'num': str(i), 'str': str(YEAR_LIST[i])})

        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def get_test_placelist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        t.append({'num': '', 'str': ''})
        yiti_len = len(SHITI_LIST)
        for i in range(1, yiti_len):
            t.append({'num': str(i), 'str': str(SHITI_LIST[i])})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def get_test_subjectlist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        t.append({'num': '', 'str': ''})
        kemu_len = len(SUBJECT_LIST)
        for i in range(1, kemu_len):
            t.append({'num': str(i), 'str': str(SUBJECT_LIST[i])})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def list_question(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('id')
        list = test_id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
            Picture.IS_TITLE: 0
        }
        pic_list = pic.getPicturebyDict(dic)
        t = []
        for item in pic_list:
            pic_dic = pic.getPictureAllDictByObject(item)
            c = {}
            c['num'] = pic_dic[Picture.NUMBER]
            c['type'] = CATEGORY_LIST[pic_dic[Picture.CATEGORY]]
            c['maxscore'] = pic_dic[Picture.SCORE]
            t.append(c)
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')
        
def remove_question(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        list = test_id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        num = int(request.POST.get('num'))
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
            Picture.NUMBER: num,
        }
        pic.removePictureIDByDic(dic)

        t = {}
        t['success']='Y'
        t['message']='ok'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def get_next_question_num(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        info = test_id
        info_list = info.split('_')
        print info_list
        year = int(info_list[0]) - YEAR_LIST[1] + 1
        province = find_item_index_in_list(info_list[1], PROVINCE_LIST)
        subject = find_item_index_in_list(info_list[2], SUBJECT_LIST)
        dict = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
            Picture.IS_TITLE: 0
        }
        pic_list = pic.getPicturebyDict(dict)
        num_list = []
        for picture in pic_list:
            info_dic = pic.getPictureAllDictByObject(picture)
            num_list.append(info_dic[Picture.NUMBER])
        num = 1
        for i in range(1, 99999):
            if i not in num_list:
                num = i
                break
        t = {'num': num}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def move_question_up(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        num = request.POST.get('num')
        # Caution: please check the boundary
        t = {}
        t['success']='N'
        t['message']='管理员正忙，没空上移'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def move_question_down(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        num = request.POST.get('num')
        # Caution: please check the boundary
        t = {}
        t['success']='N'
        t['message']='管理员正忙，没空下移'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def add_activity(request):
    # by dqn14 Nov 2, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        name = request.POST.get('name')
        date_begin = request.POST.get('date_begin')
        date_end = request.POST.get('date_end')
        teacher_id = request.POST.get('teacher_id')
        print name, date_begin, date_end
        try:
            begin_list = date_begin.split('-')
            end_list = date_end.split('-')
            back.createTimerbyDict({Timer.NAME:name,
                                    Timer.START_TIME: datetime.date(int(begin_list[0]), int(begin_list[1]), int(begin_list[2])),
                                    Timer.END_TIME: datetime.date(int(end_list[0]), int(end_list[1]), int(end_list[2])),
                                    Timer.TEACHER_ID: int(teacher_id)
                                    })
            t = {}
            t['success']='Y'
            t['message']= u'活动创建成功'
            print 't', t
            return JsonResponse(t)
        except:
            t = {}
            t['success']='N'
            t['message']=u'创建失败'
            return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def export_activity_result(request):
    # by dqn14 Nov 2, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        try:
            id = int(request.POST.get('id'))
            teacher_id = int(request.POST.get('teacher_id'))
            filename = 'files/%s_timer_%s_teacher.xls' % (str(id), str(teacher_id))
            generateTimerXLS(id, teacher_id, filename)
            t = {}
            t['success']='Y'
            t['filename']='%s_timer_%s_teacher.xls' % (str(id), str(teacher_id))
        except:
            t['success'] = 'N'
            t['filename'] = 'no'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def set_volunteer(request):
    # by dqn14 Nov 2, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        group_id = int(request.POST.get('group_id'))
        student_id_num = request.POST.get('student_num')

        vol_list = vol.getVolunteerbyField(Volunteer.STUDENT_ID, student_id_num)
        if len(vol_list) == 0:
            t = {}
            t['success'] = 'N'
            t['message'] = u'不存在这个志愿者，请重新输入学号，亲'
            return JsonResponse(t)

        volunteer = vol_list[0]
        vol_id = getattr(volunteer, Volunteer.ID)
        try:
            group = back.getGroupbyDict({Group.ID: group_id})[0]
        except:
            t = {}
            t['success'] = 'N'
            t['message'] = u'真的有这个组吗，老师？'
            return JsonResponse(t)

        vol_list = back.getGroupAllDictByObject(group)[Group.VOL_LIST].split('_')
        if '' in vol_list:
            vol_list.remove('')

        if str(vol_id) not in vol_list:
            vol_list.append(str(vol_id))

        back.setGroup(group, Group.VOL_LIST, '_'.join(vol_list))


        t = {}
        t['success']='Y'
        t['message']=u'设置成功'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')