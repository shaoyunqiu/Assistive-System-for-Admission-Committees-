# encoding=utf-8
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import redirect
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

import GenerateVerify

import sys

sys.path.append("../")
import database.teacher_backend as teacher_backend
import database.volunteer_backend as volunteer_backend
import database.student_backend as student_backend
import database.register_backend as reg
import wechat.wechat_api as we
from database.models import *

'''
    wechat login
    by byr 161110
'''
def openid(request):
    tmp = we.get_code(request)
    #print "code: " + tmp[1]
    if tmp[0] == True:
        tmp_opneid = we.get_openid_byCode(tmp[1])
        if tmp_opneid[0] == True:
            open_id = tmp_opneid[1]
            request.session['open_id'] = open_id
            print "openid: " + open_id

'''
    login & register 界面
    by byr 161003
'''
@csrf_exempt
def login(request):
    openid(request)
    return render(request, 'src/login.html')



'''
    login 表单检查
    by byr 161006
'''
@csrf_exempt
def logincheck(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('login_username', ''):
            errors.append('enter login username')
        if not request.POST.get('login_password', ''):
            errors.append('enter login password')
        if not request.POST.get('login_yzm', ''):
            errors.append('enter login yzm')
        if not errors:
            if 'student' in request.POST:
                username = request.POST.get('login_username')
                password = request.POST.get('login_password')
                yzmString = request.POST.get('login_yzm').upper()
                if (yzmString == request.session['yzmString']):
                    print ' student login'
                    (login, id) = student_backend.checkStudentPassword(username, password)
                    if login:
                        if 'open_id' in request.session:
                            stu_id = id
                            account = student_backend.idToAccountStudent(stu_id)
                            student_backend.setStudent(account, 'openid', request.session['open_id'])
                            print "#############"
                        request.session['student_id'] = int(id)
                        print 'student_id', id
                        request.session['user_name'] = username
                        #request.session['password'] = password
                        return redirect('/student/')
                    else:
                        return HttpResponse(u"<a href='/login'>学生界面登录失败啦</a>")
                else:
                    return HttpResponse(u"<a href='/login'>学生界面登录失败</a>")
            elif 'teacher' in request.POST:
                username = request.POST.get('login_username')
                password = request.POST.get('login_password')
                yzmString = request.POST.get('login_yzm').upper()
                if (yzmString == request.session['yzmString']):
                    print ' teacher login'
                    (login,id) = teacher_backend.checkTeacherPassword(username, password)
                    if login:
                        request.session['teacher_id'] = int(id)
                        request.session['user_name'] = username
                        #request.session['password'] = password
                        return redirect('/teacher/')
                    else:
                        return HttpResponse(u"a href='/login'>教师界面登录失败<</a>")
                else:
                    return HttpResponse(u"<a href='/login'>教师界面登录失败</a>")
            elif 'volunteer' in request.POST:
                username = request.POST.get('login_username')
                password = request.POST.get('login_password')
                yzmString = request.POST.get('login_yzm').upper()
                if (yzmString == request.session['yzmString']):
                    (login,id) = volunteer_backend.checkVolunteerPassword(username, password)
                    if login:
                        request.session['volunteer_id'] = id
                        request.session['user_name'] = username
                        #request.session['password'] = password
                        # return render_to_response('/student')
                        return redirect('/volunteer')
                        #return HttpResponse(u"志愿者界面")
                    else:
                        return HttpResponse(u"<a href='/login'>志愿者界面登录失败</a>")
                else:
                    return HttpResponse(u"<a href='/login'>验证码不正确</a>")
            else:
                return HttpResponse(u"<a href='/login'>请检查用户名是否存在，请检查用户名、密码、验证码是否未填</a>")
        else:
            return HttpResponse(u"<a href='/login'>请检查用户名是否存在，请检查用户名、密码、验证码是否未填</a>")
    else:
        return HttpResponse(u"<a href='/login'>请检查用户名是否存在，请检查用户名、密码、验证码是否未填</a>")


'''
    登录界面验证码生成
    by byr 161009
'''
def gnrtyzm(request, width, height):
    img, yzmString = GenerateVerify.gnrtyzm(width, height)
    request.session['yzmString'] = yzmString
    return HttpResponse(img, 'image/jpeg')

'''
    发送邮件功能
    by byr 161026
'''
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendEmail(toEmail):
    from_addr = 'bbwrld@sina.com'
    password = 'bibiworld'
    to_addr = toEmail
    smtp_server = 'smtp.sina.com'
    msg = MIMEText('清华欢迎你\n欢迎报考清华大学！\n', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'BIBIGroup <%s>' % from_addr)
    msg['To'] = _format_addr(u'亲 <%s>' % to_addr)
    msg['Subject'] = Header(u'来自早起早睡小组的问候', 'utf-8')
    '''
    	如果MIMEText()中不含中文, subject有中文, 则无法发送邮件
    	如果都不含中文, 可以发送邮件; 如果都含中文, 也可以发送邮件
    '''
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


'''
    注册功能
    by byr 161026
'''
@csrf_protect
def register(request):
    '''
    后端需要检验邀请码和相关信息
    无误后写入到数据库
    '''
    print 'commint 12121212'
    username = request.POST.get('username', '1')
    password = request.POST.get('password','2')
    email = request.POST.get('email','3')
    invited = request.POST.get('invited','4')
    print 'username : ', username

    reg_list = reg.getRegisterCodebydic({RegisterCode.REGISTER_CODE: invited, RegisterCode.STATE: 0})
    if len(reg_list) <= 0:
        print '--------------'
        return JsonResponse({'result': '验证码不可用'})

    success = student_backend.createStudent(username, {Student.PASSWORD: password, Student.EMAIL: email,
                                                       Student.REGISTER_CODE: invited})
    if success:
        reg.removeRegisterCode(invited)
        obj = RegisterCode.objects.model()
        try:
            setattr(obj, RegisterCode.REGISTER_CODE, invited)
            setattr(obj, RegisterCode.STATE, 1)
            setattr(obj, RegisterCode.ACCOUNT, username)
            obj.full_clean()
        except:
            return False
        obj.save()

    else:
        return JsonResponse({'result': '注册失败，用户名已存在'})

    print email
    if (success):
        sendEmail(email)
    return JsonResponse({'result': '注册成功'})





