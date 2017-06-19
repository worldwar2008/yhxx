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
import xlwt
from datetime import datetime
import cStringIO
from mooc.forms import UploadFileForm
from pypinyin import pinyin, lazy_pinyin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# create logger
logger = logging.getLogger("blog.views")


# Create your views here.
def prepare(request):
    return render(request, 'prepare.html')


def login(request):
    if request.user.is_authenticated():
        if Student.objects.filter(userid=request.user.id):
            # 当前是学生
            return HttpResponseRedirect('/index/show', content_type=RequestContext(request))
        elif Teacher.objects.filter(userid=request.user.id):
            # 当前是教师
            return HttpResponseRedirect('/indexteacher', content_type=RequestContext(request))


    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        logger.info(u"用户:" + username + u"试图登陆系统")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            logger.info(u"用户:" + username + u"成功登陆系统")
            if Student.objects.filter(userid=request.user.id):
                return HttpResponseRedirect('/index/show', content_type=RequestContext(request))
            elif Teacher.objects.filter(userid=request.user.id):
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
            logger.info(username + u"密码修改成功")
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
    now_date = datetime.now()
    if (now_date.month < 9):
        # 9月份之前显示上学期的课程,9月份之后显示下学期的选择的课程
        course_y = str(now_date.year-1)+"-"+str(now_date.year)
        #print "course_year",course_year
    else:
        #9月份之后,列表就会显示下学年的课程了
        course_y = str(now_date.year)+"-"+str(now_date.year+1)
        #print "course_year", course_year
    noteach = Course.objects.filter(course_teach__isnull=True)
    student = Student.objects.filter(userid=request.user.id)[0]
    student_grade = 6- ((student.graduationdate-datetime.now().date()).days/365)
    allCourse = Course.objects.filter(course_year=course_y, course_grade=student_grade).order_by('course_type')
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


def course_need_modify(request):
    """
    主要显示出, 所教授班级并没有把课程选完的同学
    :param request:
    :return:
    """

    #noteach = Course.objects.filter(course_teach__isnull=True)
    allCourse = Course.objects.all().order_by('course_type')
    tech = Teacher.objects.filter(name=request.user)

    logger.info("tech[0].department: " + tech[0].department)
    tech_grade = tech[0].department
    allStudent = Student.objects.filter(grade=tech_grade)

    student_below_5 = []

    def compute_week_time(week_time):
        num = 0
        for item in week_time:
            num += int(item.split('-')[1][0])-int(item.split('-')[0][-1])+1
        return num

    for s in allStudent:
        week_time = []
        if s.course_set.count() < 6:
            #print s.name_zh,s.course_set.count() ,s.course_set.all()
            for c in s.course_set.all():
                week_time.append(c.course_week)
            if compute_week_time(week_time) < 12:
                # for w in week_time:
                #     print s.name_zh+u"上课时间是: " + w
                student_below_5.append(s)
    #print "没有完全选课成功的人数",len(student_below_5)

    return render(request, 'student_not_enough_course.html',
                  {'student_below_5': student_below_5,'all_student':allStudent})

def course_export(request):
    """
    导出年级的课程的选课情况
    :param request:
    :return:
    """

    #noteach = Course.objects.filter(course_teach__isnull=True)
    allCourse = Course.objects.all().order_by('course_type')
    response = HttpResponse(content_type="text/html")
    response['Content-Disposition'] = 'attachment;filename=export_course_info.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(u'课程')
    #1st line   
    sheet.write(0, 0, 'grade')
    sheet.write(0, 1, 'name')
    sheet.write(0, 2, 'price')
    sheet.write(0, 3, 'year')
    sheet.write(0, 4, 'type')
    sheet.write(0, 5, 'week')
    sheet.write(0, 6, 'name_zh')
    sheet.write(0, 7, 'class_name')
    sheet.write(0, 8, 'study_stage')
    sheet.write(0, 9, 'name')

    row = 1
    for course in allCourse:
        row_value = []
        for cho in course.course_choose.all():
            row_value.append([course.course_grade,course.course_name,
                              course.course_price,course.course_year,
                              course.course_type,course.course_week,
                              cho.name_zh,cho.class_name,
                              cho.study_stage,cho.name])

        for row_i in range(len(row_value)):
            for col_i,col_value in enumerate(row_value[row_i]):
                sheet.write(row+row_i, col_i, col_value)
        row=row + len(row_value)
       
    output = cStringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response


@login_required()
def student_import(request):

    """
    按照指定的数据格式,csv类型进行学生信息的导入
    :param request:
    :return:
    """
    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        f = request.FILES['file']

        head = f.readline().rstrip('\r\n')
        if head == "name,sex,campus,study_stage,grade,class_name,birthdate,eduNumber,name_pinyin,name_zh,graduationdate":
            print "数据格式正确"
            for line in f.readlines():
                ll = line.rstrip('\r\n').split(",")
                print ll
                user = User(first_name=ll[8],
                            last_name=ll[8],
                            username=ll[7])
                user.set_password(123456)
                user.save()
                #user.delete()
                student = Student(name=ll[0],
                                  sex=unicode(ll[1]),
                                  campus=unicode(ll[2]),
                                  study_stage=unicode(ll[3]),
                                  grade=unicode(ll[4]),
                                  class_name=unicode(ll[5]),
                                  birthdate=unicode(ll[6]),
                                  eduNumber=ll[7],
                                  name_zh=unicode(ll[9]),
                                  graduationdate=unicode(ll[10]),
                                  userid=user)
                student.save()
                #student.delete()

            f.close()
            return render_to_response('msg-success-import.html', {"messages": "导入成功"}, context_instance=RequestContext(request))
        else:
            f.close()
            return render_to_response('msg-success-import.html', {"messages": "字段不全,请重新检查数据"}, context_instance=RequestContext(request))



    else:
        form = UploadFileForm()

    return render_to_response('import.html', {'form': form}, context_instance=RequestContext(request))

@login_required()
def changepwd4stu(request):
    if request.POST:
        edunumber = request.POST['q']
        students = Student.objects.filter(eduNumber=edunumber)
        if len(students)==0:
            return render_to_response("indexteacher.html",
                                      {"rlt": "你输入的教育id有误,或者此学生不存在,请重新输入"},
                                      context_instance=RequestContext(request))
        else:
            try:
                student = students[0]
                user = student.userid
                user.set_password(123456)
                user.save()
                info = [student.name_zh, "更新成功", "默认密码是:123456"]
                return render_to_response("indexteacher.html",
                                      {"rlt": " ".join(info)},
                                      context_instance=RequestContext(request))
            except Exception,e:
                print e
                return render_to_response("indexteacher.html",
                                      {"rlt": "处理有误,请重新输入"},
                                      context_instance=RequestContext(request))

@login_required()
def addgrade(request):
    if request.POST:
        try:

            students = Student.objects.all()
            for student in students:
                student.grade = str(int(student.grade[0])+1)+"年级"
                student.save()


            return render_to_response("indexteacher.html",
                                          {"ag": "升级成功"},
                                          context_instance=RequestContext(request))
        except Exception,e:
            return render_to_response("indexteacher.html",
                                          {"ag": "升级失败"},
                                          context_instance=RequestContext(request))
@login_required()
def degrade(request):
    if request.POST:
        try:
            students = Student.objects.all()
            for student in students:
                student.grade = str(int(student.grade[0])-1)+"年级"
                student.save()
            return render_to_response("indexteacher.html",
                                          {"dg": "降级成功"},
                                          context_instance=RequestContext(request))
        except Exception,e:
            return render_to_response("indexteacher.html",
                                          {"dg": "降级失败"},
                                          context_instance=RequestContext(request))

