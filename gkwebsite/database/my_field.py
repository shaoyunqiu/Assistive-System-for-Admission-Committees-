# coding:utf8
import StringIO
import json

from django.db import models
import ast
import xlwt
import os
from models import *
import student_backend as stu

from django.http import HttpResponse

MAJOR_LIST = [u'',u'计算机科学与技术系', u'电子工程系', u'自动化系', u'化学系', u'物理系']
SEX_LIST = [u'',u'男', u'女']

PROVINCE_LIST = [u'',u'北京市',u'天津市',u'河北省',u'山西省',u'内蒙古自治区',u'辽宁省',u'吉林省',u'黑龙江省',u'上海市',u'江苏省',u'浙江省',
u'安徽省',u'福建省',u'江西省',u'山东省',u'河南省',u'湖北省',u'湖南省',u'广东省',u'广西壮族自治区',u'海南省',u'重庆市',u'四川省',u'贵州省',
u'云南省',u'西藏自治区', u'陕西省',u'甘肃省',u'青海省',u'宁夏回族自治区',u'新疆维吾尔自治区',u'香港特别行政区',u'澳门特别行政区',u'台湾省',]
NATION_LIST = [u'',u'汉族', u'壮族', u'满族', u'回族', u'苗族', u'维吾尔族', u'土家族', u'彝族', u'蒙古族', u'藏族', u'布依族',
u'侗族', u'瑶族', u'朝鲜族', u'白族', u'哈尼族', u'哈萨克族', u'黎族', u'傣族', u'畲族', u'僳僳族', u'仡佬族', u'东乡族',
u'拉祜族', u'水族', u'佤族', u'纳西族', u'羌族', u'土族', u'仫佬族', u'锡伯族', u'柯尔克孜族', u'达斡尔族', u'景颇族',
u'毛南族', u'撒拉族', u'布朗族', u'塔吉克族', u'阿昌族', u'普米族', u'鄂温克族', u'怒族', u'京族', u'基诺族', u'德昂族', u'保安族',
u'俄罗斯族', u'裕固族', u'乌孜别克族',  u'门巴族',  u'鄂伦春族',  u'独龙族',  u'塔塔尔族',  u'赫哲族',  u'高山族',  u'珞巴族',]

ADMISSION_STATUS_LIST = [u'已录取', u'未投档', u'已投档']
TYPE_LIST = [u' ', u'文科', u'理科']
YEAR_LIST = [u' ', 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
SUBJECT_LIST = [u' ', u'语文', u'数学', u'英语', u'物理', u'化学', u'生物', u'理综', u'文综', u'生活', u'其他']
NUMBER_LIST = [u' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
               27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
               53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
SCORE_LIST = [u' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
               27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
               53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
CATEGORY_LIST = [u' ', u'主观', u'客观']
SHITI_LIST = PROVINCE_LIST

def get_picture_path(year, province, subject, number, score, category):
    return str(year) + '_' + str(province) + '_' + str(subject) + '_' + str(number) + '_' + str(score) + '_' + str(category)

def find_item_index_in_list(item, list):
    chang = len(list)
    for i in range(0, chang):
        if item == list[i]:
            return i
    return -1


class ListField(models.TextField):
    #__metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if not value:
            value = []

        if isinstance(value, list):
            return value
        # print 'caocao',type(ast.literal_eval(value))
        # print ast.literal_eval(value)
        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        # print 'caca  ', type(value)
        # return value
        return unicode(value)  # use str(value) in Python 3

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)



def outputXLS(path, filename, sheet, list, _titleList):
    '''
    输出注册码到excel，会自动在第一列增加序号1-n
    :param path: 导出的路径，目前没有到这个参数
    :param filename: xls的文件名
    :param sheet: sheet名称
    :param list: 二位数组[[],[],[]],其中的每个list都是1列
    :return:是否成功创建
    '''
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    num = len(list[0])
    for item in list:
        if len(item) != num:
            return False

    tmplist = []
    for i in range(1, num + 1):
        tmplist.append(i)
    mylist = [tmplist] + list
    titleList = [u'序号']
    for item in _titleList:
        titleList.append(item)
    print titleList

    if len(titleList) != len(mylist):
        return False

    for i in range(0,len(titleList)):
        sh.write(0, i, titleList[i])

    for i in range(0, len(mylist)):
        for j in range(0, len(mylist[i])):
            sh.write(j + 1, i, mylist[i][j])
    book.save(filename)
    return True


def generateExcel(request,id, path, filename, sheet, list, _titleList):
    filename = "files/%s_teacher.xls" % id
    if os.path.exists(filename):
        os.remove(filename)
    outputXLS(path, filename, sheet, list, _titleList)


def getStudentEstimateScore(student):
    tmp_dic = getattr(student, 'estimate', '{}')
    try:
        tmp_dic = eval(tmp_dic)
    except:
        tmp_dic = eval('{}')
    sum_score = 0
    for key in tmp_dic.keys():
        if 'shenhe' in tmp_dic[key].keys():
            sum_score += tmp_dic[key]['score']
    return str(sum_score)

def getStudentEstimateRank(student):
    score = int(getStudentEstimateScore(student))
    if score == 0:
        return 'You do not have score!'
    all_student_estimate_score = [999999]
    student_list = stu.getAllInStudent()
    for item in student_list:
        all_student_estimate_score.append(getStudentEstimateScore(item))

    rank = 1
    ranked_score_list = sorted(all_student_estimate_score, reverse=True)

    length = len(ranked_score_list)
    for i in range(0, length):
        if score >= ranked_score_list[i]:
            rank = i
            break

    return str(rank)














