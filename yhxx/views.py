# coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib import messages
from mooc.models import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.contrib.auth import update_session_auth_hash
import logging


# create logger
logger=logging.getLogger("blog.views")

# Create your views here.
def prepare(request):
    return render(request, 'prepare.html')


def login(request):
    if request.user.is_authenticated():
        if Student.objects.filter(userid=request.user.id):
            # 当前是学生
            return HttpResponseRedirect('/index/show', content_type=RequestContext(request))
        else:
            # 当前是教师
            return HttpResponseRedirect('/indexteacher', content_type=RequestContext(request))

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        logger.info(u"用户:"+username+u"试图登陆系统")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            logger.info(u"用户:"+username+u"成功登陆系统")
            if Student.objects.filter(userid=request.user.id):
                return HttpResponseRedirect('/index/show', content_type=RequestContext(request))
            else:
                return HttpResponseRedirect('/indexteacher', content_type=RequestContext(request))
        else:
            return render_to_response('login-pwd-error.html', context_instance=RequestContext(request))
    else:

        return render_to_response('login.html', context_instance=RequestContext(request))


def indexstudent(request):
    return render(request, 'indexstudent.html')


def indexteacher(request):
    return render(request, 'indexteacher.html')


def schedule(request):
    return render(request, 'schedule.html')


def grade(request):
    return render(request, 'grade.html')


def choose(request):
    return render(request, 'choose.html')


def bill(request):
    return render(request, 'bill.html')


def news(request):
    return render(request, 'news.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/', content_type=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/', content_type=RequestContext(request))
    else:
        form = UserCreationForm()
    return render_to_response('register.html', locals(), context_instance=RequestContext(request))


@login_required
def change_pwd(request, username,
                    template_name='change_pwd.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):


    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one if
            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
            # is enabled.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/accounts/change_pwd_done/')
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': 'Password change',
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

@login_required
def change_pwd_done(request, username='',
                    template_name='pwd_change_done.html',
                    current_app=None, extra_context=None):

    context = {
        'title': 'Password change successful',
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

def course_canceled(request):
    # 主要是需要筛选掉选课人数不足的学生,这些学生的课程自动释放;
    # 如果选课人数满足要求,则这些学生的课则不能再动了;
    noteach = Course.objects.filter(course_teach__isnull=True)
    allCourse = Course.objects.all().order_by('course_type')
    insuffStu = []
    for c in allCourse:
        if c.course_min_num == 0:
            pass
        elif c.course_choose.count() < c.course_min_num:
            insuffStu.append(c)
    above_min_num_classes = []
    for c in allCourse:
        if c.course_min_num == 0:
            pass
        elif c.course_choose.count() >= c.course_min_num:
            above_min_num_classes.append(c)
    above_min_num_count = []
    for c in allCourse:
        if c.course_min_num == 0:
            pass
        elif c.course_choose.count() >= c.course_min_num:
            above_min_num_count.append(c.course_choose.count())

    return render(request, 'course_canceled_meihua.html',
                  {'noteach': noteach, 'insuffStu': insuffStu, 'above_min_num_classes': above_min_num_classes,
                   'above_min_num_count': above_min_num_count})
