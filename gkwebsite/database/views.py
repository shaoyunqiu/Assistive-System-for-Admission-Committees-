# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from models import *
import student_backend as stu
import teacher_backend as tch


# Create your views here.

def search_student_by_name(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        name = request.POST.get('name')
        stu_list = stu.getStudentbyField(Student.REAL_NAME, name)
        # search for students in database
        for item in stu_list:
            dic = {'id': getattr(item, 'id'),
                   'name': getattr(item, Student.REAL_NAME, 'no such attr. by evan69'),
                   'gender': getattr(item, Student.SEX),
                   'source': getattr(item, Student.PROVINCE),
                   'school': getattr(item, Student.SCHOOL),
                   'id_card': getattr(item, Student.ID_NUMBER)}
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
        #	DELETE FROM student WHERE id=/%request.POST.get('id')%/
        return JsonResponse({})  # return nothing
    else:
        return HttpResponse('Access denied.')


def student_list_all(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        '''
		c = {'id':'151099','name':'王二', 'gender':'男', 'source':'北京', 'school':'人大附中', 'id_card':'11010819980824181X'}
		# SELECT * FROM student
		t = []
		t.append(c)
		d = {'id':'151016','name':'张三', 'gender':'男', 'source':'湖北', 'school':'黄冈中学', 'id_card':'520108199808241894'}
		t.append(d)
		e = {'id':'152357','name':'李四', 'gender':'女', 'source':'湖北', 'school':'黄冈中学', 'id_card':'520108199808241864'}
		t.append(e)
		f = {'id':'159930','name':'阿不来提·阿卜杜热西提', 'gender':'男', 'source':'新疆', 'school':'乌鲁木齐市第一中学', 'id_card':'86010819980824187X'}
		t.append(f)
		'''
        stu_list = stu.getAllInStudent()
        # search for students in database
        for item in stu_list:
            dic = {'id': getattr(item, 'id'),
                   'name': getattr(item, Student.REAL_NAME),
                   'gender': getattr(item, Student.SEX),
                   'source': getattr(item, Student.PROVINCE),
                   'school': getattr(item, Student.SCHOOL),
                   'id_card': getattr(item, Student.ID_NUMBER)}
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def get_teacher_name_by_id(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = tch.idToAccountTeacher(id)
        #	SELECT FROM teacher WHERE id=/%request.POST.get('id')%/
        # name = "世界"
        t = {'name': tch.getTeacher(account, 'realName')}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def search_volunteer_by_name(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        c = {'id': '151099', 'name': '王二', 'department': '电机工程与应用电子技术系', 'class': '电51', 'student_id': '2015010874'}
        c['name'] = request.POST.get('name')
        t.append(c)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def remove_volunteer_by_id(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        #	DELETE FROM student WHERE id=/%request.POST.get('id')%/
        return JsonResponse({})  # return nothing
    else:
        return HttpResponse('Access denied.')


def volunteer_list_all(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []

        c = {'id': '151099', 'name': '王二', 'department': '电机工程与应用电子技术系', 'class': '电51', 'student_id': '2015010874'}
        # SELECT * FROM student
        t = []
        t.append(c)
        d = {'id': '151016', 'name': '张三', 'department': '化学系', 'class': '化学51', 'student_id': '2015012874'}
        t.append(d)
        e = {'id': '152357', 'name': '李四', 'department': '工程物理系', 'class': '核31', 'student_id': '2013012079'}
        t.append(e)
        f = {'id': '159930', 'name': 'Giannis Antetokounmpo', 'department': '苏世民书院', 'class': '苏6',
             'student_id': '2016080123'}
        t.append(f)

        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def add_student(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        num = request.POST.get('num')
        c = {'code': 'DEADBEEF'}
        d = {'code': '1A0083F9'}
        t = []
        t.append(c)
        t.append(d)
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')
