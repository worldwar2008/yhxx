#! -*- coding:utf-8 -*-
"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
import issue:
    要注意,在下面的匹配里面,如果后面多加一个斜杠/,会造成在选课的时候还是跳转到mooc_list的页面里面
"""
from django.conf.urls import include, url
from views import *
urlpatterns = [
    url(r'^$', mooc_list, name='mooc_list'),
    url(r'^(?P<stu_user_id>\d+)/show_stu_course', show_stu_course, name='show_stu_courses'),
    url(r'^(?P<course_time>\d+)/(?P<stu_user_id>\d+)/show_stu_mooc_list', show_stu_mooc_list, name='show_stu_mooc_list'),
    url(r'^(?P<id>\d+)/(?P<stu_user_id>\d+)/show_stu_mooc_detail$', show_stu_mooc_detail, name='show_stu_mooc_detail'),
    url(r'^(?P<id>\d+)/(?P<stu_user_id>\d+)/show_stu_add$', show_stu_course_add, name='show_stu_course_add'),
    url(r'^(?P<id>\d+)/(?P<stu_user_id>\d+)/show_stu_delete$', show_stu_course_delete, name='show_stu_course_delete'),


    url(r'^(?P<course_time>\d+)/mooc_list$', mooc_list, name='mooc_list'),
    url(r'^(?P<id>\d+)/$', mooc_detail, name='mooc_detail'),
    url(r'^(?P<id>\d+)/add$', course_add, name='course_add'),
    url(r'^(?P<id>\d+)/delete$', course_delete, name='course_delete'),
    url(r'^(?P<id>\d+)/mates$', show_who_choose_this_class, name='show_who_choose_this_class'),

]
