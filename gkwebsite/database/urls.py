from django.conf.urls import *
from . import views

urlpatterns = [
	url(r'^search_student_by_name/$', views.search_student_by_name, name="search_student_by_name"),
	url(r'^remove_student_by_id/$', views.remove_student_by_id, name="remove_student_by_id"),
	url(r'^student_list_all/$', views.student_list_all, name="student_list_all"),
	url(r'^get_teacher_name_by_id/$', views.get_teacher_name_by_id, name="get_teacher_name_by_id"),
	url(r'^search_volunteer_by_name/$', views.search_volunteer_by_name, name="search_volunteer_by_name"),
	url(r'^remove_volunteer_by_id/$', views.remove_volunteer_by_id, name="remove_volunteer_by_id"),
	url(r'^volunteer_list_all/$', views.volunteer_list_all, name="volunteer_list_all"),
	url(r'^add_student/$', views.add_student, name="add_student"),
	url(r'^add_volunteer/$', views.add_volunteer, name="add_volunteer")
	]