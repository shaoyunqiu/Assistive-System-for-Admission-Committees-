from django.test import TestCase
from models import Teacher
from teacher_backend import *

# Create your tests here.

def startTest():
    deleteAll()
    createAccountTest()
    checkAccountTest()
    checkColomnTest()
    getDataTest()

def createAccountTest():
    print '*******************'
    print 'createAccount'
    print 'account bug here'
    dic = {'account': 'houyf##', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf'}
    createAccount(dic)
    dic = {'account': '#!@houyf', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'hou@@yf', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'ho', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    print 'account right here'
    dic = {'account': 'houyf1', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'houyf2', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    print 'account occupied here'
    dic = {'account': 'houyf3', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)

    print '-------------------------------------------------'
    print 'email bug here'
    dic = {'account': 'houyf141', 'password': 'mima', 'area': 'wuhan', 'email': '@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'houyf142', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'houyf143', 'password': 'mima', 'area': 'wuhan', 'email': 'aqq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    print 'email right here'
    dic = {'account': 'houyf144', 'password': 'mima', 'area': 'wuhan', 'email': '11112222@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)

def checkAccountTest():
    print '*******************'
    print 'checkAccount'
    print 'False here'
    print checkAccount('houyf1')
    print checkAccount('houyf144')
    print 'True here'
    print checkAccount('houyf##')
    print checkAccount('lihy')

def checkColomnTest():
    print '*******************'
    print 'checkColomn'
    print 'True here'
    print checkColomn('account')
    print checkColomn('password')
    print checkColomn('area')
    print checkColomn('email')
    print checkColomn('phone')
    print checkColomn('realName')
    print checkColomn('volunteerList')
    print 'False here'
    print checkColomn('none')

def getAccountTest():
    pass

def getDataTest():
    print '*******************'
    print 'getData'
    print getData('houyf1','password')
    print getData('houyf2','area')
    print 'None here'
    print getData('houyf4','area')
    print getData('houyf2', 'are')

def setDataTest():
    print '*******************'
    print 'setData'
