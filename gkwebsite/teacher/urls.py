from django.conf.urls import *

urlpatterns = [
    url(r'^$', teacher_py.userinfo.index),
    ]
