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
		#d = {'id':'151016','name':'张三', 'gender':'男', 'source':'湖北', 'school':'黄冈中学', 'id_card':'520108199808241894'}
		name = request.POST.get('name')
		stu_list = stu.getStudentbyField(Student.REAL_NAME,name)
		# search for students in database
		for item in stu_list:
			dic = {'id':getattr(item,'id'),
				   'name':getattr(item,Student.REAL_NAME,'no such attr. by evan69'),
				   'gender':getattr(item,Student.SEX),
				   'source':getattr(item,Student.PROVINCE),
				   'school':getattr(item,Student.SCHOOL),
				   'id_card':getattr(item,Student.ID_NUMBER)}
			t.append(dic)
		return JsonResponse(t, safe=False)	# must use 'safe=False'
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
		return JsonResponse({})	# return nothing
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
		return JsonResponse(t, safe=False)	# must use 'safe=False'
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
		#name = "世界"
		t={'name':tch.getTeacher(account,'realName')}
		return JsonResponse(t)
	else:
		return HttpResponse('Access denied.')