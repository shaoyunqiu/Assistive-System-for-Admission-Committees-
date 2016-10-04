from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

# Create your views here.

def student_center(request):
	t = get_template('student/center.html')
	c = Context({'name': 'duanqn'})
	return HttpResponse(t.render(c))