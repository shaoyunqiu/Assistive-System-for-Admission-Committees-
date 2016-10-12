#coding:utf8
from django.test import TestCase
from models import Teacher
import teacher_backend as tch

# Create your tests here.

def startTest():
    tch.deleteAll()
    createAccountTest()
    checkAccountTest()
    checkColomnTest()
    getDataTest()

def createTestAccount():
    tch.deleteAll()
    dic = {'account': 'houyf1', 'password': 'mima', 'area': 'wuhan', 'email': 'a1@qq.com', 'phone': '11111111',
           'realName': u'张三', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'houyf2', 'password': 'mima', 'area': 'wuhan', 'email': 'a2@qq.com', 'phone': '11111111',
           'realName': u'李四', 'volunteerList': ['c', 'd']}
    tch.createAccount(dic)
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'a3@qq.com', 'phone': '11111111',
           'realName': u'王五', 'volunteerList': ['e', 'f']}
    tch.createAccount(dic)

def createAccountTest():
    print '*******************'
    print 'createAccount'
    print 'account bug here'
    dic = {'account': 'houyf##', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf'}
    tch.createAccount(dic)
    dic = {'account': '#!@houyf', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'hou@@yf', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'ho', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    print 'account right here'
    dic = {'account': 'houyf1', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com',
           'realName': u'hehe', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'houyf2', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': u'白仁', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': u'呵呵', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'houyf4', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': u"李阳", 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    print 'account occupied here'
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)

    print '-------------------------------------------------'
    print 'email bug here'
    dic = {'account': 'houyf141', 'password': 'mima', 'area': 'wuhan', 'email': '@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'houyf142', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    dic = {'account': 'houyf143', 'password': 'mima', 'area': 'wuhan', 'email': 'aqq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)
    print 'email right here'
    dic = {'account': 'houyf144', 'password': 'mima', 'area': 'wuhan', 'email': '11112222@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    tch.createAccount(dic)

def checkAccountTest():
    print '*******************'
    print 'checkAccount'
    print 'False here'
    print tch.checkAccount('houyf1')
    print tch.checkAccount('houyf144')
    print 'True here'
    print tch.checkAccount('houyf##')
    print tch.checkAccount('lihy')

def checkColomnTest():
    print '*******************'
    print 'checkColomn'
    print 'True here'
    print tch.checkColomn('account')
    print tch.checkColomn('password')
    print tch.checkColomn('area')
    print tch.checkColomn('email')
    print tch.checkColomn('phone')
    print tch.checkColomn('realName')
    print tch.checkColomn('volunteerList')
    print 'False here'
    print tch.checkColomn('none')

def getAccountTest():
    pass

def getDataTest():
    print '*******************'
    print 'getData'
    print tch.getData('houyf1','password')
    print tch.getData('houyf2','area')
    print 'None here'
    print tch.getData('houyf4','area')
    print tch.getData('houyf2', 'are')

def setDataTest():
    print '*******************'
    print 'setData'
