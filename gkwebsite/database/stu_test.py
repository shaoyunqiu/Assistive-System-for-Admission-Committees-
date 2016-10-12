#coding:utf8
from student_backend import *
import datetime
def testCreateStudent():
    # createStudent("lihy", {Student.CLASSROOM: 'jiaoshi', Student.REAL_NAME: 'lihaoyang'})
    createStudent("lihy11", {Student.ID_NUMBER: '123456789123456789',Student.SCHOOL:u'南山中学', Student.PROVINCE:12, Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX:1,Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('lihaoyang0', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren0', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang1', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren1', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang2', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren2', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang3', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren3', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang4', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren4', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang5', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren5', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang6', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren6', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang7', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren7', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang8', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren8', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang9', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                 Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                 Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren9', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                 Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                 Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang10',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren10',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang11',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren11',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang12',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren12',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang13',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren13',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang14',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren14',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang15', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren15', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang16', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren16', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang17', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren17', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang18', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren18', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang19', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren19', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang20', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren20', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang21', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren21', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang22', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren22', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang23', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren23', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang24', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren24', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang25',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren25',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang26',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren26',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang27',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren27',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang28',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren28',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang29',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren29',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang30', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren30', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang31', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren31', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang32', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren32', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang33', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren33', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang34', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren34', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang35', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren35', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang36', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren36', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang37', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren37', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang38', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren38', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang39', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren39', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang40',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren40',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang41',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren41',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang42',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren42',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang43',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren43',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang44',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren44',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang45', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren45', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang46', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren46', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang47', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren47', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang48', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren48', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang49', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren49', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang50', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren50', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang51', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren51', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang52', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren52', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang53', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren53', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang54', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren54', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang55',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren55',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang56',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren56',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang57',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren57',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang58',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren58',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang59',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren59',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang60', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren60', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang61', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren61', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang62', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren62', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang63', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren63', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang64', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren64', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang65', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren65', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang66', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren66', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang67', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren67', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang68', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren68', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang69', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren69', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang70',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren70',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang71',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren71',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang72',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren72',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang73',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren73',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang74',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren74',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang75', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren75', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang76', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren76', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang77', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren77', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang78', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren78', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang79', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren79', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang80', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren80', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang81', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren81', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang82', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren82', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang83', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren83', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang84', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren84', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang85',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren85',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 10,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang86',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren86',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 11,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang87',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren87',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 12,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang88',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren88',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 13,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang89',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                   Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren89',
                  {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 14,
                   Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                   Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang90', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren90', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 0,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang91', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren91', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 1,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang92', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren92', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 2,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang93', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren93', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 3,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang94', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren94', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 4,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang95', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren95', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 5,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang96', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren96', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 6,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang97', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren97', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 7,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang98', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren98', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 8,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})
    createStudent('lihaoyang99', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一1班', Student.REAL_NAME: u'李昊阳', Student.SEX: 1,
                                  Student.BIRTH: datetime.datetime(2015, 1, 12)})
    createStudent('baiyunren99', {Student.ID_NUMBER: '123456789123456789', Student.SCHOOL: u'南山中学', Student.PROVINCE: 9,
                                  Student.CLASSROOM: u'高一2班', Student.REAL_NAME: u'白云仁', Student.SEX: 2,
                                  Student.BIRTH: datetime.datetime(2018, 1, 12)})

    return True
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
