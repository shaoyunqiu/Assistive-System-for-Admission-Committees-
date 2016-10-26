from django.conf.urls import *
from . import views

urlpatterns = [
	url(r'^search_student_by_name/$', views.search_student_by_name, name="search_student_by_name"),
	url(r'^remove_student_by_id/$', views.remove_student_by_id, name="remove_student_by_id"),
	url(r'^student_list_all/$', views.student_list_all, name="student_list_all"),
	url(r'^get_teacher_name_by_id/$', views.get_teacher_name_by_id, name="get_teacher_name_by_id"),
	url(r'^get_volunteer_name_by_id/$', views.get_volunteer_name_by_id, name="get_volunteer_name_by_id"),
	url(r'^search_volunteer_by_name/$', views.search_volunteer_by_name, name="search_volunteer_by_name"),
	url(r'^remove_volunteer_by_id/$', views.remove_volunteer_by_id, name="remove_volunteer_by_id"),
	url(r'^volunteer_list_all/$', views.volunteer_list_all, name="volunteer_list_all"),
	url(r'^add_student/$', views.add_student, name="add_student"),
	url(r'^add_volunteer/$', views.add_volunteer, name="add_volunteer"),
    url(r'^export_registration_code/$', views.export_registration_code, name="export_registration_code"),
    url(r'^get_teacher_alert_by_id/$', views.get_teacher_alert_by_id, name="get_teacher_alert_by_id"),
    url(r'^test_list_all/$', views.test_list_all, name="test_list_all"),
    url(r'^release_test/$', views.release_test, name="release_test"),
    url(r'^remove_test/$', views.remove_test, name="remove_test"),
    url(r'^withdraw_test/$', views.withdraw_test, name="withdraw_test"),
    url(r'^add_test/$', views.add_test, name="add_test"),
    url(r'^get_test_yearlist/$', views.get_test_yearlist, name="get_test_yearlist"),
    url(r'^get_test_placelist/$', views.get_test_placelist, name="get_test_placelist"),
    url(r'^get_test_subjectlist/$', views.get_test_subjectlist, name="get_test_subjectlist"),
    
	]