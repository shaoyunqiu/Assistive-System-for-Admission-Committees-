from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader,Context
from django.shortcuts
#from login.login.teacher import userinfo ? for example

user = {}

@csrf_exempt

def index(request):
    #from the login get the user info, and response to the userinfo,html list
