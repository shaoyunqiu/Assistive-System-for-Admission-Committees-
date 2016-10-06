# encoding=utf-8
from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

'''
    login & register 界面
    by byr 161003
'''


def login(request):
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
                return HttpResponse(u"学生界面")
            elif 'teacher' in request.POST:
                return HttpResponse(u"教师界面")
            elif 'volunteer' in request.POST:
                return HttpResponse(u"志愿者界面")
            else:
                return render_to_response('src/login.html');
    else:
        return render_to_response('src/login.html',
                                  {'errors': errors});
