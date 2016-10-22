from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import redirect

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.

def student_center(request):
    t = get_template('student/center.html')
    id = request.session.get('user_id', -1)
    c = {'id': id}
    return HttpResponse(t.render(c))


def student_score(request):
    t = get_template('student/score.html')
    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')
    c = {'id': id}
    return HttpResponse(t.render(c))


def student_rank(request):
    t = get_template('student/rank.html')
    return HttpResponse(t.render({}))


def student_admit(request):
    t = get_template('student/admit.html')
    return HttpResponse(t.render({}))


def student_contact(request):
    t = get_template('student/contact.html')
    return HttpResponse(t.render({}))


def student_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('/login')


def profile(request):
    return render(request, 'student/userinfo.html')

@csrf_exempt
def get_all_tests(request):
    # if 'user_id' not in request.session.keys():
    #    return redirect('/login/')
    dic = {'tests' : ['a','b','c']}
    return JsonResponse(dic)
