# coding:utf8
import StringIO
import json

from django.db import models
import ast
import xlwt
import os

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
TYPE_LIST = [u'文科', u'理科']

def majorIntToString(num):
    return num
    #index = num % len(MAJOR_LIST)
    #return MAJOR_LIST[index]

def sexIntToString(num):
    return num
    #index = num % len(SEX_LIST)
    #return SEX_LIST[index]

def provinceIntToString(num):
    return num
    #index = num % len(PROVINCE_LIST)
    #return PROVINCE_LIST[index]

def nationIntToString(num):
    return num
    #index = num % len(NATION_LIST)
    #return NATION_LIST[index]

def admissionStatusIntToString(num):
    return num
    #index = num % len(ADMISSION_STATUS_LIST)
    #return ADMISSION_STATUS_LIST[index]

def typeIntToString(num):
    #index = num % len(TYPE_LIST)
    return num
    #return TYPE_LIST[index]





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

    filename = "%s_Report.xls" % id

    if os.path.exists('./%s_Report.xls' % id):
        excel = open("%s_Report.xls" % id, "r")
        output = StringIO.StringIO(excel.read())
        out_content = output.getvalue()
        output.close()
        response = HttpResponse(out_content,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=%s_Report.xls' % id
        return response
    else:
        result = outputXLS(path, filename, sheet, list, _titleList)
        if result:
            excel = open("%s_Report.xls" % id, "r")
            output = StringIO.StringIO(excel.read())
            out_content = output.getvalue()
            output.close()
            response = HttpResponse(out_content,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=%s_Report.xls' % id
            return response
        else:
            return HttpResponse(json.dumps({"no":"excel","no one": "cries"}))