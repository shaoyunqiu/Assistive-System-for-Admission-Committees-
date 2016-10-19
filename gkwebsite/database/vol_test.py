#coding:utf8
from volunteer_backend import *
import datetime

def testCreateVolunteer():
    # createVolunteer("lihy", {Volunteer.CLASSROOM: 'jiaoshi', Volunteer.REAL_NAME: 'lihaoyang'})
    createVolunteer("vol1", {Volunteer.ID_NUMBER: '123456789123456789',Volunteer.SCHOOL:u'南山中学', Volunteer.PROVINCE:12,
                             Volunteer.CLASSROOM: u'高一1班', Volunteer.REAL_NAME: u'李昊阳',
                             Volunteer.SEX:1,Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang1', 'baiyunren1']})
    createVolunteer('vol2', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 0,
                                 Volunteer.CLASSROOM: u'高一1班', Volunteer.REAL_NAME: u'侯禺凡', Volunteer.SEX: 1,
                                 Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang2', 'baiyunren2']})
    createVolunteer('vol3', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 0,
                                 Volunteer.CLASSROOM: u'高一2班', Volunteer.REAL_NAME: u'邵韵秋', Volunteer.SEX: 2,
                                 Volunteer.BIRTH: datetime.datetime(2018, 1, 12),
                                 Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang3', 'baiyunren3']})
    createVolunteer('vol4', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 1,
                                 Volunteer.CLASSROOM: u'高一1班', Volunteer.REAL_NAME: u'侯禺凡', Volunteer.SEX: 1,
                                 Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang4', 'baiyunren4']})
    createVolunteer('vol5', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 1,
                                 Volunteer.CLASSROOM: u'高一2班', Volunteer.REAL_NAME: u'邵韵秋', Volunteer.SEX: 2,
                                 Volunteer.BIRTH: datetime.datetime(2018, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang5', 'baiyunren5']})
    createVolunteer('vol6', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 2,
                                 Volunteer.CLASSROOM: u'高一1班', Volunteer.REAL_NAME: u'侯禺凡', Volunteer.SEX: 1,
                                 Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                                 Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang6', 'baiyunren6']})
