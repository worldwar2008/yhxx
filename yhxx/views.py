# coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mooc.models import *
from django.contrib.auth.decorators import login_required


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
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
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
