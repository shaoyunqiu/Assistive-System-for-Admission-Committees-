from django.conf.urls import *
from . import views

urlpatterns = [
	url(r'^search_student_by_name/$', views.search_student_by_name, name="search_student_by_name"),
	url(r'^remove_student_by_id/$', views.remove_student_by_id, name="remove_student_by_id"),
	url(r'^student_list_all/$', views.student_list_all, name="student_list_all"),
	url(r'^get_teacher_name_by_id/$', views.get_teacher_name_by_id, name="get_teacher_name_by_id"),
	]