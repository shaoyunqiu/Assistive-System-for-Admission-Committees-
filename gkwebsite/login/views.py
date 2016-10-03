#encoding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
    login 界面
    by byr 161003
'''
def login(request):
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return render(request, 'src/login.html')
