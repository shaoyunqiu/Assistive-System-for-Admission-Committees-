#coding:utf8
from django.test import TestCase
from models import Teacher
import teacher_backend as tch
import student_backend as stu
import volunteer_backend as vol
import register_backend as reg
import image_backend as img


from vol_test import  *
from stu_test import *



def createData():
    tch.deleteTeacherAll()
    stu.deleteStudentAll()
    vol.deleteVolunteerAll()
    reg.deleteRegisterCodeAll()
    img.deletePictureAll()

    createTestData()
    testCreateVolunteerNew()
    testCreateStudentNew()

# Create your tests here.

def startTest():
    tch.deleteTeacherAll()
    createAccountTest()
    checkAccountTest()
    checkColomnTest()
    getDataTest()

def createTestData():
    tch.deleteTeacherAll()
    dic = {'account': 'houyf1', 'password': 'mima', 'area': u'北京', 'email': 'nsu@math.thu.edu.cn', 'phone': '13901684995',
           'realName': u'苏宁', 'volunteerList': ['vol1', 'vol2', 'vol3', 'vol4', 'vol5']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf2', 'password': 'mima', 'area': u'广东', 'email': 'sywang@mail.tsinghua.edu.cn', 'phone': '18815750324',
           'realName': u'王山鹰', 'volunteerList': ['vol1', 'vol2', 'vol3', 'vol4', 'vol5']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf3', 'password': 'mima', 'area': u'广西', 'email': 'sunjg@mail.tsinghua.edu.cn', 'phone': '13825669941',
           'realName': u'孙家广', 'volunteerList': ['vol1', 'vol2', 'vol3', 'vol4', 'vol5']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf4', 'password': 'mima', 'area': u'新疆', 'email': 'liss02@tsinghua.edu.cn', 'phone': '17877766432',
           'realName': u'李山山', 'volunteerList': ['vol1', 'vol2', 'vol3', 'vol4', 'vol5']}
    tch.createTeacher(dic)

def createAccountTest():
    # print '*******************'
    # print 'createAccount'
    # print 'account bug here'
    dic = {'account': 'houyf##', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf'}
    tch.createTeacher(dic)
    dic = {'account': '#!@houyf', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'hou@@yf', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'ho', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    # print 'account right here'
    dic = {'account': 'houyf1', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com',
           'realName': u'hehe', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf2', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': u'白仁', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': u'呵呵', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf4', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': u"李阳", 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    # print 'account occupied here'
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)

    # print '-------------------------------------------------'
    # print 'email bug here'
    dic = {'account': 'houyf141', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf142', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    dic = {'account': 'houyf143', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)
    # print 'email right here'
    dic = {'account': 'houyf144', 'password': 'mima', 'area': 'wuhan', 'email': 'alienlhy@163.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createTeacher(dic)

def checkAccountTest():
    # print '*******************'
    # print 'checkAccount'
    # print 'False here'
    tch.checkTeacherAccount('houyf1')
    tch.checkTeacherAccount('houyf144')
    # print 'True here'
    tch.checkTeacherAccount('houyf##')
    tch.checkTeacherAccount('lihy')

def checkColomnTest():
    # print '*******************'
    # print 'checkColomn'
    # print 'True here'
    tch.checkTeacherField('account')
    tch.checkTeacherField('password')
    tch.checkTeacherField('area')
    tch.checkTeacherField('email')
    tch.checkTeacherField('phone')
    tch.checkTeacherField('realName')
    tch.checkTeacherField('volunteerList')
    # print 'False here'
    tch.checkTeacherField('none')

def getAccountTest():
    pass

def getDataTest():
    # print '*******************'
    # print 'getData'
    tch.getTeacher('houyf1','password')
    tch.getTeacher('houyf2','area')
    # print 'None here'
    tch.getTeacher('houyf_notexist','area')
    tch.getTeacher('houyf2', 'are')

def setDataTest():
    # print '*******************'
    # print 'setData'
    pass
