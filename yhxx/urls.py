"""yhxx URL Configuration

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
"""
from django.conf.urls import include, url
from django.contrib import admin
import mooc.views
from views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^indexstudent/$', indexstudent, name='indexstudent'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^accounts/change_pwd/(?P<username>\w+)/$', change_pwd, name='change_pwd'),
    url(r'^accounts/change_pwd_done/$', change_pwd_done, name='change_pwd'),

    url(r'^accounts/schedule/$', schedule, name='schedule'),
    url(r'^accounts/grade/$', grade, name='grade'),
    url(r'^accounts/choose/$', choose, name='choose'),
    url(r'^accounts/news/$', news, name='news'),
    url(r'^accounts/bill/$', bill, name='bill'),
    # url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name='login'),
    # url(r'^accounts/logout/$', logout, {'template_name': 'index.html'}, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    # url(r'^$', index, name='index'),
    url(r'^$', login, name='login'),
    url(r'^mooc/', include('mooc.urls')),
    url(r'^index/show$', mooc.views.show_my_course, name='show_my_course'),
    url(r'^indexstudent$', indexstudent, name='indexstudent'),
    url(r'^indexteacher$', indexteacher, name='indexteacher'),
    url(r'^changepwd4stu', changepwd4stu, name='changepwd4stu'),
    url(r'^addgrade', addgrade, name='addgrade'),
    url(r'^degrade', degrade, name='degrade'),
    url(r'^course_canceled$', course_canceled, name='course_canceled'),
    url(r'^course_need_modify$', course_need_modify, name='course_modify'),
    url(r'^course_export$', course_export, name='course_export'),
    url(r'^students_import$', student_import, name='student_import'),
    url(r'^show_scores$', mooc.views.show_scores, name='show_scores'),
    url(r'^set_scores/(?P<id>\d+)$', mooc.views.set_scores, name='set_scores'),
]
