from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

# Create your views here.

def student_center(request):
	t = get_template('student/center.html')
	c = Context({'person_name': 'John Smith',
		'company': 'Outdoor Equipment',
		'ship_date': datetime.date(2009, 4, 2),
		'ordered_warranty': False})
	return HttpResponse(t.render(c))