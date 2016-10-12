#coding:utf8
from student_backend import *
import datetime
def testCreateStudent():
    # createStudent("lihy", {Student.CLASSROOM: 'jiaoshi', Student.REAL_NAME: 'lihaoyang'})
    return createStudent("lihy2",{Student.CLASSROOM:'jiaoshi',Student.REAL_NAME:'lihaoyang',
                                 Student.BIRTH:datetime.datetime(2015, 1, 12)})
def testGetStudent():
    print getStudent('lihy2',Student.REAL_NAME)
    print getStudent('lihy2', Student.BIRTH)
    print getStudent('lihy123', Student.BIRTH)
    print getStudent('lihy123', 'a')

def testSetStudent():
    print setStudent('lihy2',Student.REAL_NAME,u'李昊阳')
    print getStudent('lihy2', Student.REAL_NAME)
    print setStudent('lihy2', Student.BIRTH, datetime.datetime(1996, 4, 5))
    print getStudent('lihy2', Student.BIRTH)

def testTranStudent():
    print idToAccountStudent(getStudent('lihy2',Student.ID))
    print accountToIDStudent('lihy2')
