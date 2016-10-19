# coding:utf8
import StringIO
import json

from django.db import models
import ast
import xlwt
import os

from django.http import HttpResponse

MAJOR_LIST = [u'', u'计算机科学与技术系', u'电子工程系', u'自动化系', u'化学系', u'物理系']
SEX_LIST = [u'',u'男', u'女']
PROVINCE_LIST = [u'', u'北京', u'上海', u'内蒙古', u'江苏', u'湖北', u'广东', u'广西']
NATION_LIST = [u'', u'汉族', u'蒙古族', u'壮族', u'彝族', u'维吾尔族', u'兽族', u'不死族']


def majorIntToString(num):
    index = num % len(MAJOR_LIST)
    return MAJOR_LIST[index]

def sexIntToString(num):
    index = num % len(SEX_LIST)
    return SEX_LIST[index]

def provinceIntToString(num):
    index = num % len(PROVINCE_LIST)
    return PROVINCE_LIST[index]

def nationIntToString(num):
    index = num % len(NATION_LIST)
    return NATION_LIST[index]



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

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

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