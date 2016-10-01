from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.student_center, name='student_center'),
]