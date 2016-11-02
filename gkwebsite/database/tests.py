from django.test import TestCase
from django.test.utils import setup_test_environment
from models import *
import traceback
from django.core.exceptions import ValidationError
from my_field import *
import backend as back
from student_backend import *
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
