from django.test import TestCase
from django.test.utils import setup_test_environment
from models import *
import traceback
from django.core.exceptions import ValidationError
from my_field import *
import backend as back
from student_backend import *
from teacher_backend import *
from back_test import *

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



