from django.test import TestCase
from models import Teacher
from teacher_backend import *

# Create your tests here.

def createAccountTest():
    print 'account bug here'
    dic = {'account': 'houyf##', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
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
    dic = {'account': 'houyf', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'houyf3424', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
    dic = {'account': 'h2o432uyf', 'password': 'mima', 'area': 'wuhan', 'email': 'a@qq.com', 'phone': '11111111',
           'realName': 'hyf', 'volunteerList': ['a', 'b']}
    createAccount(dic)
