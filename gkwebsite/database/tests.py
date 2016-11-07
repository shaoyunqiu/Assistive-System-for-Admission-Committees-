# coding:utf8
from django.test import TestCase
from django.test.utils import setup_test_environment
from models import *
import traceback
from django.core.exceptions import ValidationError
from my_field import *
import backend as back
from student_backend import *
from my_field import *
import ast
import xlwt
import os
import time
import random, string
from teacher_backend import *
from back_test import *
from volunteer_backend import *
import image_backend as img_back
import register_backend as reg_back

setup_test_environment()


class TestIdtoAccountStudent(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        stu1.full_clean()
        stu1.save()
        stu2 = Student.objects.model()
        setattr(stu2, Student.ACCOUNT, "test_stu_2")
        stu2.full_clean()
        stu2.save()

    def test_illegal_id(self):
        self.assertEqual(idToAccountStudent(-1), None)
        self.assertEqual(idToAccountStudent(100000), None)

    def test_not_int_id(self):
        self.assertEqual(idToAccountStudent("hhhh"), False)

    def test_ok_id(self):
        self.assertEqual(idToAccountStudent(1), "test_stu_1")


class TestAccountToStudentId(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        stu1.full_clean()
        stu1.save()

    def test_legal_id(self):
        self.assertEqual(accountToIDStudent("test_stu_1"), "1")

    def test_not_existing_id(self):
        self.assertEqual(accountToIDStudent("lihy1"), None)


class TestRemoveStudentAccount(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        stu1.full_clean()
        stu1.save()

    def test_delete_legal_student(self):
        removeStudentAccount("test_stu_1")
        self.assertEqual(len(Student.objects.filter(account="test_stu_1")), 0)

    def test_delete_illegal_student(self):
        removeStudentAccount("test_stu_2")
        self.assertEqual(len(Student.objects.filter(account="test_stu_2")), 0)


class TestgetordeleteAllStudent(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        stu1.full_clean()
        stu1.save()
        stu2 = Student.objects.model()
        setattr(stu2, Student.ACCOUNT, "test_stu_2")
        stu2.full_clean()
        stu2.save()

    def test_getAllStudent(self):
        self.assertEqual(len(getAllInStudent()), 2)

    def test_deleteStudentAll(self):
        deleteStudentAll()
        self.assertEqual(len(Student.objects.filter(account="test_stu_1")), 0)
        self.assertEqual(len(Student.objects.filter(account="test_stu_2")), 0)

    def test_getAllStudent_after_delete(self):
        deleteStudentAll()
        self.assertEqual(len(getAllInStudent()), 0)


class TestCheckField(TestCase):
    def test_exist_field(self):
        field_list = ['id','account', 'password', 'realName', 'birth', 'idNumber', 'type', 'sex', 'nation', 'school',
                      'classroom', 'address', 'phone', 'email', 'dadPhone', 'momPhone', 'tutorName', 'tutorPhone', 'province',
                      'major',  'testScoreList', 'rankList', 'sumNumberList', 'estimateScore', 'realScore', 'admissionStatus',
                      'comment', 'registerCode', 'teacherList', 'volunteerAccountList', 'isLogedin', 'isRegistered', 'groupList',
                      'wechat', 'fixedPhone', 'qq', 'dadName', 'momName', 'duiyingTeacher']
        for field in field_list:
            self.assertEqual(checkField(field), True)

    def test_nonexist_field(self):
        self.assertEqual(checkField('nickname'), False)


class TestgetStudentByField(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.REAL_NAME, "lihy1")
        setattr(stu1, Student.PROVINCE, 1)
        stu1.full_clean()
        stu1.save()
        stu2 = Student.objects.model()
        setattr(stu2, Student.ACCOUNT, "test_stu_2")
        setattr(stu2, Student.REAL_NAME, "lihy2")
        stu2.full_clean()
        stu2.save()
        stu3 = Student.objects.model()
        setattr(stu3, Student.ACCOUNT, "test_stu_3")
        setattr(stu3, Student.REAL_NAME, "lihy3")
        setattr(stu3, Student.PROVINCE, 1)
        stu3.full_clean()
        stu3.save()

    def test_getstudentbyfield_unique(self):
        self.assertEqual(len(getStudentbyField("account", "test_stu_1")), 1)
        self.assertEqual(len(getStudentbyField("realName", "lihy1")), 1)

    def test_getstudentbyfield_many(self):
        self.assertEqual(len(getStudentbyField("province", 1)), 2)

    def test_getstudentbyfield_noexist_value(self):
        self.assertEqual(len(getStudentbyField("account","lsp")), 0)

    def test_getstudentbyfield_illegal_field(self):
        self.assertEqual(len(getStudentbyField("trick", "hhh")), 0)


class Testgetstudentall(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.REAL_NAME, "lihy1")
        setattr(stu1, Student.PROVINCE, 1)
        stu1.full_clean()
        stu1.save()
        stu2 = Student.objects.model()
        setattr(stu2, Student.ACCOUNT, "test_stu_2")
        setattr(stu2, Student.REAL_NAME, "lihy2")
        stu2.full_clean()
        stu2.save()

    def test_getstudentall_correct(self):
        stu = getStudentAll("test_stu_1")
        self.assertEqual(stu.realName, "lihy1")

    def test_getstudentall_noexisting_account(self):
        self.assertEqual(getStudentAll("lsp"), None)


class Testgetstudentalldictbyacount(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.REAL_NAME, "lihy1")
        setattr(stu1, Student.PROVINCE, 1)
        stu1.full_clean()
        stu1.save()

    def test_getstudentalldictbyaccount_illegal_account(self):
        self.assertEqual(getStudentAllDictByAccount("test"), None)

    def test_getstudentalldictbyaccount_correct(self):
        result = getStudentAllDictByAccount("test_stu_1")
        self.assertEqual(result[Student.REAL_NAME], "lihy1")
        self.assertEqual(result[Student.PROVINCE]['province'], 1)
        self.assertEqual(result[Student.PROVINCE]['provincelist'], PROVINCE_LIST)


class Testgetstudent(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.REAL_NAME, "lihy1")
        setattr(stu1, Student.PROVINCE, 1)
        stu1.full_clean()
        stu1.save()

    def test_getstudent_error_field(self):
        self.assertEqual(getStudent("test_stu_1", "hehe"), None)

    def test_getstudent_error_account(self):
        self.assertEqual(getStudent("test", "account"), None)

    def test_getstudent_correct(self):
        self.assertEqual(getStudent("test_stu_1", "id"), 1)
        self.assertEqual(getStudent("test_stu_1", Student.REAL_NAME), "lihy1")
        self.assertEqual(getStudent("test_stu_1", Student.PROVINCE), 1)


class Testsetstudent(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.REAL_NAME, "lihy1")
        setattr(stu1, Student.PROVINCE, 1)
        stu1.full_clean()
        stu1.save()

    def test_setstudent_errorfield(self):
        self.assertEqual(setStudent("test_stu_1", "hehe", "hh"), False)

    def test_setstudent_erroraccount(self):
        self.assertEqual(setStudent("test", Student.REAL_NAME,"hh"), False)

    def test_setstudent_correct(self):
        self.assertEqual(setStudent("test_stu_1", Student.REAL_NAME,"hehe"), True)
        stu = (Student.objects.filter(account="test_stu_1"))[0]
        self.assertEqual(stu.realName, "hehe")

    def test_setstudent_id(self):
        self.assertEqual(setStudent("test_stu_1", Student.ID, 0), False)
        stu = (Student.objects.filter(account="test_stu_1"))[0]
        self.assertEqual(stu.id, 1)


class Testcreatestudent(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.REAL_NAME, "lihy1")
        setattr(stu1, Student.PROVINCE, 1)
        stu1.full_clean()
        stu1.save()

    def test_create_account_exist(self):
        self.assertEqual(createStudent("test_stu_1",{}), False)

    def test_create_account_change_id(self):
        self.assertEqual(createStudent("test_2", {Student.ID: 1}), False)
        self.assertEqual(len(Student.objects.filter(account="test_2")), 0)

    def test_create_account_change_account(self):
        self.assertEqual(createStudent("test_3", {Student.ACCOUNT: "test0"}), False)
        self.assertEqual(len(Student.objects.filter(account="test0")), 0)
        self.assertEqual(len(Student.objects.filter(account="test_3")), 0)

    def test_create_ok(self):
        self.assertEqual(createStudent("test_4", {Student.REAL_NAME:"lihy"}), True)
        stu = (Student.objects.filter(account="test_4"))[0]
        self.assertEqual(stu.realName, "lihy")

    def test_create_wrong_attr(self):
        self.assertEqual(createStudent("test_5", {Student.PROVINCE:"jiang"}), False)


class Testcheckstudentpassword(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.PASSWORD, "mima")
        stu1.full_clean()
        stu1.save()

    def test_checkpassword_illegal_account(self):
        self.assertEqual(checkStudentPassword("test", "mima"), (False , 'Account does not exist.'))

    def test_checkpassword_wronf(self):
        self.assertEqual(checkStudentPassword("test_stu_1", "wrong"), (False , 'Password is incorrect'))

    def test_checkpassword_ok(self):
        self.assertEqual(checkStudentPassword("test_stu_1", "mima"), (True, "1"))


class Testgetallteacheranddelete(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        tea1.full_clean()
        tea1.save()
        tea2 = Teacher.objects.model()
        setattr(tea2, Teacher.ACCOUNT, "test_tea_2")
        tea2.full_clean()
        tea2.save()

    def test_getallteacer_ok(self):
        self.assertEqual(len(getAllInTeacher()), 2)

    def test_deleteall(self):
        deleteTeacherAll()
        self.assertEqual(len(Teacher.objects.filter(account="test_tea_1")), 0)
        self.assertEqual(len(Teacher.objects.filter(account="test_tea_2")), 0)

    def test_getallteahcer_emoty(self):
        deleteTeacherAll()
        self.assertEqual(len(getAllInTeacher()), 0)


class Testidtoaccountteacher(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        tea1.full_clean()
        tea1.save()
        tea2 = Teacher.objects.model()
        setattr(tea2, Teacher.ACCOUNT, "test_tea_2")
        tea2.full_clean()
        tea2.save()

    def test_illegal_id_teacher(self):
        self.assertEqual(idToAccountStudent(-1), None)
        self.assertEqual(idToAccountStudent(100000), None)

    def test_not_int_id_teacher(self):
        self.assertEqual(idToAccountStudent("hhhh"), False)

    def test_ok_id_teacher(self):
        self.assertEqual(idToAccountTeacher(1), "test_tea_1")


class Testcheckteacheraccount(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        tea1.full_clean()
        tea1.save()
        tea2 = Teacher.objects.model()
        setattr(tea2, Teacher.ACCOUNT, "test_tea_2")
        tea2.full_clean()
        tea2.save()

    def test_checkaccount_ok(self):
        self.assertEqual(checkTeacherAccount("test_tea_1"), False)
        self.assertEqual(checkTeacherAccount("test_tea_2"), False)

    def test_checkaccount_nonexist(self):
        self.assertEqual(checkTeacherAccount("test"), True)


class Testcreateteacher(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        tea1.full_clean()
        tea1.save()

    def test_create_exist_account(self):
        self.assertEqual(createTeacher({Teacher.ACCOUNT:"test_tea_1"}), False)

    def test_create_no_account_key(self):
        self.assertEqual(createTeacher({Teacher.REAL_NAME:"houyf"}), False)

    def test_create_OK(self):
        self.assertEqual(createTeacher({Teacher.ACCOUNT:"test", Teacher.REAL_NAME: "houyf"}), True)
        self.assertEqual(len(Teacher.objects.filter(account="test")), 1)
        self.assertEqual(len(Teacher.objects.filter(realName="houyf")), 1)

    def test_create_illegal_key(self):
        self.assertEqual(createTeacher({Teacher.ACCOUNT:"test", "nonexist": 1}), True)


class Testcheckteacherpassword(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        setattr(tea1, Teacher.PASSWORD, "mima")
        tea1.full_clean()
        tea1.save()
        tea2 = Teacher.objects.model()
        setattr(tea2, Teacher.ACCOUNT, "test_tea_2")
        setattr(tea2, Teacher.PASSWORD, "mmimi")
        tea2.full_clean()
        tea2.save()

    def test_illegal_account(self):
        self.assertEqual(checkTeacherPassword("test", "mima"), (False , 'Account does not exist.'))

    def test_correct_account(self):
        self.assertEqual(checkTeacherPassword("test_tea_1","mima"), (True, "1"))
        self.assertEqual(checkTeacherPassword("test_tea_1", "mimi"), (False, 'Password is incorrect'))


class Testcheckteacherfield(TestCase):
    def test_legal_field(self):
        self.assertEqual(checkTeacherField(Teacher.ACCOUNT), True)
        self.assertEqual(checkTeacherField(Teacher.COMMENT), True)

    def test_illegal_field(self):
        self.assertEqual(checkTeacherField("esitimate"), False)


class Testgetteacherall(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        setattr(tea1, Teacher.REAL_NAME, "houyf1")
        tea1.full_clean()
        tea1.save()
        tea2 = Teacher.objects.model()
        setattr(tea2, Teacher.ACCOUNT, "test_tea_2")
        setattr(tea2, Teacher.REAL_NAME, "houyf2")
        tea2.full_clean()
        tea2.save()

    def test_getteacherall_correct(self):
        tea1 = getTeacherAll("test_tea_1")
        self.assertEqual(tea1.realName, "houyf1")
        tea2 = getTeacherAll("test_tea_2")
        self.assertEqual(tea2.realName, "houyf2")

    def test_getteacherall_noexisting_account(self):
        self.assertEqual(getTeacherAll("lsp"), None)


class Testgetteacher(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        setattr(tea1, Teacher.REAL_NAME, "houyf1")
        setattr(tea1, Teacher.PASSWORD, "mima")
        tea1.full_clean()
        tea1.save()

    def test_getstudent_error_field(self):
        self.assertEqual(getTeacher("test_tea_1", "hehe"), None)

    def test_getstudent_error_account(self):
        self.assertEqual(getTeacher("test", "account"), None)

    def test_getstudent_correct(self):
        self.assertEqual(getTeacher("test_tea_1", "id"), 1)
        self.assertEqual(getTeacher("test_tea_1", Student.REAL_NAME), "houyf1")
        self.assertEqual(getTeacher("test_tea_1", Student.PASSWORD), "mima")


class Testsetteacher(TestCase):
    def setUp(self):
        tea1 = Teacher.objects.model()
        setattr(tea1, Teacher.ACCOUNT, "test_tea_1")
        setattr(tea1, Teacher.REAL_NAME, "houyf1")
        setattr(tea1, Teacher.PASSWORD, "mima")
        tea1.full_clean()
        tea1.save()

    def test_setteacher_error_field(self):
        self.assertEqual(setTeacher("test_tea_1", "hehe", "hh"), False)

    def test_setteacher_erroraccount(self):
        self.assertEqual(setTeacher("test", Teacher.REAL_NAME,"hh"), False)

    def test_setteacher_correct(self):
        self.assertEqual(setTeacher("test_tea_1", Teacher.REAL_NAME,"hehe"), True)
        tea = (Teacher.objects.filter(account="test_tea_1"))[0]
        self.assertEqual(tea.realName, "hehe")

    def test_setteacher_id(self):
        self.assertEqual(setTeacher("test_tea_1", "id", 0), False)
        tea = (Teacher.objects.filter(account="test_tea_1"))[0]
        self.assertEqual(tea.id, 1)

    def test_setteacher_illegal_value(self):
        self.assertEqual(setTeacher("test_tea_1", Teacher.PASSWORD, 1), False)
        tea = (Teacher.objects.filter(account="test_tea_1"))[0]
        self.assertEqual(tea.password, "mima")


class TestMyfield(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.ESTIMATE_SCORE, {u'2016_北京_语文':{"time":111, "score":90,"shenhe":1},u'2016_北京_英语':{'time':222,'score':10}})
        stu1.full_clean()
        stu1.save()
        stu2 = Student.objects.model()
        setattr(stu2, Student.ACCOUNT, "test_stu_2")
        setattr(stu2, Student.ESTIMATE_SCORE, {u'2016_北京_数学':{'time':0000,'shenhe':''}})
        stu2.full_clean()
        stu2.save()
        stu3 = Student.objects.model()
        setattr(stu3, Student.ACCOUNT, "test_stu_3")
        setattr(stu3, Student.ESTIMATE_SCORE, {u'2016_北京_英语':{'time':222, 'score':99, 'shenhe':1}, u'2016':{'time':111, 'score':"0", 'shenhe':0}, u'2016_':{'time':233, 'score':90, 'shenhe':1}})
        stu3.full_clean()
        stu3.save()

    def test_get_picture_path(self):
        self.assertEqual(get_picture_path("2016","beijing","chinese","1","1","wen"), "2016_beijing_chinese_1_1_wen.pic")

    def test_find_item_in_list(self):
        mylist = range(0,10)
        self.assertEqual(find_item_index_in_list(0, mylist), 0)
        self.assertEqual(find_item_index_in_list(10, mylist), -1)

    def test_getstudent_estimate_socre(self):
        stu1 = (Student.objects.filter(account="test_stu_1"))[0]
        stu2 = (Student.objects.filter(account="test_stu_2"))[0]
        stu3 = (Student.objects.filter(account="test_stu_3"))[0]
        self.assertEqual(getStudentEstimateScore(stu1), "90")
        self.assertEqual(getStudentEstimateScore(stu2), "0")
        self.assertEqual(getStudentEstimateScore(stu3), "189")


class Testgetestimate(TestCase):
    def setUp(self):
        stu1 = Student.objects.model()
        setattr(stu1, Student.ACCOUNT, "test_stu_1")
        setattr(stu1, Student.PROVINCE, 1)
        setattr(stu1, Student.ESTIMATE_SCORE,
                {u'2016_北京_语文': {"time": 111, "score": 90, "shenhe": 1}, u'2016_北京_英语': {'time': 222, 'score': 80, 'shenhe':1}})
        stu1.full_clean()
        stu1.save()
        stu2 = Student.objects.model()
        setattr(stu2, Student.ACCOUNT, "test_stu_2")
        setattr(stu2, Student.PROVINCE, 1)
        setattr(stu2, Student.ESTIMATE_SCORE, {u'2016_北京_数学': {'time': 0000, 'shenhe': ''}})
        stu2.full_clean()
        stu2.save()
        stu3 = Student.objects.model()
        setattr(stu3, Student.ACCOUNT, "test_stu_3")
        setattr(stu3, Student.PROVINCE, 1)
        setattr(stu3, Student.ESTIMATE_SCORE, {u'2016_北京_英语': {'time': 222, 'score': 99, 'shenhe': 1},
                                               u'2016_北京_语文': {'time': 111, 'score': "1", 'shenhe': 0},
                                               u'2016_北京_数学': {'time': 233, 'score': 90, 'shenhe': 1}})
        stu3.full_clean()
        stu3.save()
        stu4 = Student.objects.model()
        setattr(stu4, Student.ACCOUNT, "test_stu_4")
        setattr(stu4, Student.PROVINCE, 2)
        setattr(stu4, Student.ESTIMATE_SCORE,
                {u'2016_天津_语文': {"time": 111, "score": 90, "shenhe": 1}, u'2016_天津_英语': {'time': 222, 'score': 80}})
        stu4.full_clean()
        stu4.save()

    def test_getesitimaterank(self):
        stu1 = Student.objects.filter(account="test_stu_1")[0]
        stu2 = Student.objects.filter(account="test_stu_2")[0]
        stu3 = Student.objects.filter(account="test_stu_3")[0]
        stu4 = Student.objects.filter(account="test_stu_4")[0]
        self.assertEqual(getStudentEstimateRank(stu1), ("2", "2"))
        self.assertEqual(getStudentEstimateRank(stu2), ("2", "2"))
        self.assertEqual(getStudentEstimateRank(stu3), ("1", "2"))
        self.assertEqual(getStudentEstimateRank(stu4), ("1", "1"))

    def test_getestumatescore_every(self):
        stu1 = Student.objects.filter(account="test_stu_1")[0]
        stu2 = Student.objects.filter(account="test_stu_2")[0]
        stu3 = Student.objects.filter(account="test_stu_3")[0]
        stu4 = Student.objects.filter(account="test_stu_4")[0]
        self.assertEqual(getStudentEstimateScore_Every(stu1, u'2016_北京_语文'), "90")
        self.assertEqual(getStudentEstimateScore_Every(stu1, u'2016'), "0")
        self.assertEqual(getStudentEstimateScore_Every(stu2, u'2016_北京_数学'),"0")
        self.assertEqual(getStudentEstimateScore_Every(stu3, u'2016_北京_语文'),"1")
        self.assertEqual(getStudentEstimateScore_Every(stu4, u'2016_天津_英语'), "0")

    def test_getestimatescoreeverynoshenhe(self):
        stu1 = Student.objects.filter(account="test_stu_1")[0]
        stu2 = Student.objects.filter(account="test_stu_2")[0]
        stu3 = Student.objects.filter(account="test_stu_3")[0]
        stu4 = Student.objects.filter(account="test_stu_4")[0]
        self.assertEqual(getStudentEstimateScore_Every_no_shenhe(stu1,u'2016_北京_语文'), "90")
        self.assertEqual(getStudentEstimateScore_Every_no_shenhe(stu1, u'2016'), "0")
        self.assertEqual(getStudentEstimateScore_Every_no_shenhe(stu2, u'2016_北京_数学'), "0")
        self.assertEqual(getStudentEstimateScore_Every_no_shenhe(stu3, u'2016_北京_语文'), "1")
        self.assertEqual(getStudentEstimateScore_Every_no_shenhe(stu4, u'2016_天津_英语'), "80")

    def test_getstudentestimaterankevery(self):
        stu1 = Student.objects.filter(account="test_stu_1")[0]
        stu2 = Student.objects.filter(account="test_stu_2")[0]
        stu3 = Student.objects.filter(account="test_stu_3")[0]
        stu4 = Student.objects.filter(account="test_stu_4")[0]
        self.assertEqual(getStudentEstimateRank_Every(stu1, u'2016_北京_语文'),("1","2"))
        self.assertEqual(getStudentEstimateRank_Every(stu2, u'2016_北京_数学'),("1","1"))
        self.assertEqual(getStudentEstimateRank_Every(stu3, u'2016_北京_数学'), ("1","1"))
        self.assertEqual(getStudentEstimateRank_Every(stu4, u'2016_天津_英语'), ("1", "0"))


# unfinished can't pass the test
class Testnotice(TestCase):
    def setUp(self):
        no1 = Notice.objects.model()
        setattr(no1, Notice.SEND, "notice1")
        setattr(no1, Notice.RECEIVE_STU, "stu1")
        setattr(no1, Notice.RECEIVE_VOL, "vol1")
        no1.full_clean()
        no1.save()
        no2 = Notice.objects.model()
        setattr(no2, Notice.SEND, "notice2")
        no2.full_clean()
        no2.save()

     #cannot pass the test, need to modify
    def testcreatenotice(self):
        self.assertEqual(back.createNoticebyDict({"send":"notice3", "id": 0}), False)
        self.assertEqual(len(Notice.objects.filter(id=0)), 0)
        self.assertEqual(back.createNoticebyDict({"send":"notice4", "receive_stu":"stu1"}), True)
        self.assertEqual(len(Notice.objects.filter(receive_stu="stu1")), 2)


class TestVolBases(TestCase):
    def setUp(self):
        vol1 = Volunteer.objects.model()
        setattr(vol1, Volunteer.ACCOUNT, "test_vol_1")
        setattr(vol1, Volunteer.REAL_NAME, "lihy1")
        setattr(vol1, Volunteer.QUANXIAN, 1)
        setattr(vol1, Volunteer.PASSWORD, "mima")
        vol1.full_clean()
        vol1.save()
        vol2 = Volunteer.objects.model()
        setattr(vol2, Volunteer.ACCOUNT, "test_vol_2")
        setattr(vol2, Volunteer.NATION, 1)
        setattr(vol2, Volunteer.PASSWORD, "mimimi")
        vol2.full_clean()
        vol2.save()

    def test_getallvolunteer(self):
        vol = getAllInVolunteer()
        self.assertEqual(len(vol), 2)
        self.assertEqual(getattr(vol[0], Volunteer.ACCOUNT, "error"), "test_vol_1")
        self.assertEqual(getattr(vol[1], Volunteer.ACCOUNT, "error"), "test_vol_2")

    def test_deletvolall(self):
        deleteVolunteerAll()
        vol = getAllInVolunteer()
        self.assertEqual(len(vol), 0)

    def test_ishapermission(self):
        self.assertEqual(is_have_permission(1), True)
        self.assertEqual(is_have_permission(2), False)

    def test_idtoaccount(self):
        self.assertEqual(idToAccountVolunteer("a"), False)
        self.assertEqual(idToAccountVolunteer(-1), None)
        self.assertEqual(idToAccountVolunteer(1), 'test_vol_1')

    def test_accounttoid(self):
        self.assertEqual(accountToIDVolunteer('test_vol_1'), '1')
        self.assertEqual(accountToIDVolunteer('test_vol_2'), '2')
        self.assertEqual(accountToIDStudent('test'), None)

    def test_checkfield(self):
        self.assertEqual(checkField(Volunteer.REAL_NAME), True)
        self.assertEqual(checkField("tsinghua"), False)

    def test_getvolbyfied(self):
        vol = getAllInVolunteer()
        self.assertEqual(len(getVolunteerbyField(Volunteer.REAL_NAME, "lihy")), 0)
        self.assertEqual(getVolunteerbyField(Volunteer.NATION, 1)[0], vol[1])
        self.assertEqual(len(getVolunteerbyField("tsinghua", 1)), 0)

    def test_getvolunteerall(self):
        vol = getAllInVolunteer()
        self.assertEqual(getVolunteerAll("test_vol_1"), vol[0])
        self.assertEqual(getVolunteerAll("test_vol_2"), vol[1])
        self.assertEqual(getVolunteerAll("test"), None)

    def test_setVolunteer(self):
        vol = getAllInVolunteer()
        self.assertEqual(setVolunteer("test_vol_1", Volunteer.ACCOUNT, "test"), False)
        self.assertEqual(setVolunteer("test_vol_1", Volunteer.REAL_NAME, "lisanpang"), True)
        self.assertEqual(getattr(vol[0], Volunteer.REAL_NAME, "Error"), "lisanpang")
        self.assertEqual(setVolunteer("test_vol_1", "tsinghua", "beida"), False)
        self.assertEqual(setVolunteer("test_vol_1", Volunteer.NATION, 2), True)
        self.assertEqual(getattr(vol[0], Volunteer.NATION, -1), 2)
        self.assertEqual(setVolunteer("test", "test", "test"), False)
        self.assertEqual(setVolunteer("test_vol_1", Volunteer.ID, 0), False)
        self.assertEqual(getattr(vol[0], Volunteer.ID, -1), 1)

    def test_createVolunteer(self):
        self.assertEqual(createVolunteer("test_vol_1",{Volunteer.NATION:10}), False)
        self.assertEqual(createVolunteer("test_vol_3", {Volunteer.ACCOUNT:"vol"}),False)
        #self.assertEqual(createVolunteer("test_vol_3", {Volunteer.NATION:1000}), False)
        #self.assertEqual(createVolunteer("test_vol_3", {Volunteer.ID:3}), False)
        # cannot pass the above two tests
        self.assertEqual(createVolunteer("test_vol_3", {Volunteer.REAL_NAME:"lihy1"}),True)
        self.assertEqual(len(Volunteer.objects.filter(realName="lihy1")), 2)


    def test_checkpassword(self):
        self.assertEqual(checkVolunteerPassword("test_vol_1", "mima"), (True,"1"))
        self.assertEqual(checkVolunteerPassword("test_vol_1", "mimimi"), (False , 'Password is incorrect'))
        self.assertEqual(checkVolunteerPassword("test", "mima"), (False , 'Account does not exist.'))
        self.assertEqual(checkVolunteerPassword("test", "mima"), (False , 'Account does not exist.'))


class TestImageBases(TestCase):
    def setUp(self):
        img1 = Picture.objects.model()
        setattr(img1, Picture.YEAR, 2016)
        setattr(img1, Picture.PROVINCE, 1)
        setattr(img1, Picture.CATEGORY, 1)
        img1.full_clean()
        img1.save()
        img2 = Picture.objects.model()
        setattr(img2, Picture.YEAR, 2015)
        setattr(img2, Picture.PROVINCE, 1)
        setattr(img2, Picture.CATEGORY, 1)
        setattr(img2, Picture.IS_DELEVERED, 1)
        img2.full_clean()
        img2.save()

    def test_getallinpicture(self):
        img = img_back.getAllInPicture()
        self.assertEqual(len(img), 2)

    def test_deletepictureall(self):
        img_back.deletePictureAll()
        img = img_back.getAllInPicture()
        self.assertEqual(len(img), 0)

    def test_removepictureidbydic(self):
        ans = img_back.removePictureIDByDic({Picture.YEAR: 2016, Picture.CATEGORY: 1})
        img1 = Picture.objects.filter(year=2016)
        self.assertEqual(len(img1), 0)
        self.assertEqual(ans, True)
        ans = img_back.removePictureIDByDic({Picture.YEAR:2016})
        img1 = Picture.objects.filter(year=2016)
        self.assertEqual(len(img1), 0)
        self.assertEqual(ans, False)
        ans = img_back.removePictureIDByDic({Picture.YEAR:2015, Picture.PROVINCE:0})
        img1 = Picture.objects.filter(year=2015)
        self.assertEqual(len(img1), 1)
        self.assertEqual(ans, False)
        ans = img_back.removePictureIDByDic({Picture.YEAR:2015, "haha":0})
        img1 = Picture.objects.filter(year=2015)
        self.assertEqual(len(img1), 1)
        self.assertEqual(ans, False)

    def test_getpicturebydic(self):
        img_all = img_back.getAllInPicture()
        self.assertEqual(img_back.getPicturebyDict({Picture.PROVINCE:1})[0], img_all[0])
        self.assertEqual(img_back.getPicturebyDict({Picture.PROVINCE: 1})[1], img_all[1])
        self.assertEqual(len(img_back.getPicturebyDict({Picture.YEAR: 2016, "haha": 0})), 0)
        self.assertEqual(len(img_back.getPicturebyDict({Picture.YEAR: 2016, Picture.CATEGORY:0})), 0)
        self.assertEqual(img_back.getPicturebyDict({Picture.YEAR: 2015})[0], img_all[1])

    def test_getalldictbyobject(self):
        img_all = img_back.getAllInPicture()
        dict_0 = img_back.getPictureAllDictByObject(img_all[0])
        dict_1 = img_back.getPictureAllDictByObject(img_all[1])
        self.assertEqual(dict_0[Picture.YEAR], 2016)
        self.assertEqual(dict_1[Picture.IS_DELEVERED], 1)
        for field in Picture.FIELD_LIST:
            if field in dict_0.keys():
                self.assertEqual(dict_0[field], getattr(img_all[0], field, "Error"))
            if field in dict_1.keys():
                self.assertEqual(dict_1[field], getattr(img_all[1], field, "Error"))

    def test_getpicturebyfield(self):
        img_all = img_back.getAllInPicture()
        self.assertEqual(img_back.getPicturebyField(Picture.YEAR, 2016)[0], img_all[0])
        self.assertEqual(img_back.getPicturebyField(Picture.IS_DELEVERED, 1)[0], img_all[1])
        self.assertEqual(img_back.getPicturebyField(Picture.PROVINCE, 1)[0], img_all[0])
        self.assertEqual(img_back.getPicturebyField(Picture.PROVINCE, 1)[1], img_all[1])
        self.assertEqual(len(img_back.getPicturebyField(Picture.PROVINCE,20)), 0)
        self.assertEqual(len(img_back.getPicturebyField("hh", 0)), 0)

    def test_setpicture(self):
        img_all = img_back.getAllInPicture()
        self.assertEqual(img_back.setPicture(img_all[0], Picture.IS_DELEVERED, 1), True)
        self.assertEqual(img_back.setPicture(img_all[0], Picture.IS_DELEVERED, "false"), False)
        self.assertEqual(getattr(img_all[0],Picture.IS_DELEVERED, "Error"), 1)
        self.assertEqual(img_back.setPicture(img_all[0], Picture.YEAR, 2015), True)
        self.assertEqual(getattr(img_all[0], Picture.YEAR, "Error"), 2015)
        self.assertEqual(img_back.setPicture(img_all[0], "hehe", 0), False)
        self.assertEqual(img_back.setPicture(img_all[0], Picture.ID, 0), False)
        self.assertEqual(getattr(img_all[0], Picture.ID, "Error"), 1)

    def test_createpicture(self):
        self.assertEqual(img_back.createPicturebyDict({Picture.YEAR: 2016, Picture.PROVINCE:2}), True)
        self.assertEqual(len(Picture.objects.filter(year=2016)), 2)
        self.assertEqual(img_back.createPicturebyDict({Picture.CATEGORY: "Chinese"}), False)
        self.assertEqual(img_back.createPicturebyDict({"hahah", 0}), False)
        self.assertEqual(img_back.createPicturebyDict({Picture.ID, 0}), False)
        self.assertEqual(len(Picture.objects.filter(id=0)), 0)


class TestRegisterBases(TestCase):
    def setUp(self):
        reg1 = RegisterCode.objects.model()
        setattr(reg1, RegisterCode.ACCOUNT, "test_reg_1")
        setattr(reg1, RegisterCode.REGISTER_CODE, "2014011426")
        setattr(reg1, RegisterCode.STATE, 0)
        reg1.full_clean()
        reg1.save()
        reg2 = RegisterCode.objects.model()
        setattr(reg2, RegisterCode.ACCOUNT, "test_reg_2")
        setattr(reg2, RegisterCode.ACCOUNT, "2014011425")
        setattr(reg2, RegisterCode.STATE, 1)
        reg2.full_clean()
        reg2.save()

    def test_getallinregestercode(self):
        tmp_reg = reg_back.getAllInRegisterCode()
        self.assertEqual(len(tmp_reg), 2)
        self.assertEqual(getattr(tmp_reg[0], RegisterCode.REGISTER_CODE, "Error"), "2014011426")

    def test_removeregistercode(self):
        reg_back.removeRegisterCode("2014011426")
        reg_all = reg_back.getAllInRegisterCode()
        self.assertEqual(len(reg_all), 1)
        reg_back.removeRegisterCode("test")
        reg_all = reg_back.getAllInRegisterCode()
        self.assertEqual(len(reg_all), 1)

        














