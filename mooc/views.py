# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from mooc.models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from forms import *
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User


# Create your views here.


@login_required
def mooc_list(request, course_time):
    tmp_time = str(course_time)
    tmp_week = ""

    if tmp_time[0]=="1":
        tmp_week+= "周一"
    elif tmp_time[0]=="2":
        tmp_week+= "周二"
    elif tmp_time[0]=="3":
        tmp_week+="周三"
    elif tmp_time[0]=="4":
        tmp_week+="周四"
    elif tmp_time[0]=="5":
        tmp_week+="周五"

    if tmp_time[1:]=="56":
        tmp_week+="(5-6节)"
    elif tmp_time[1:]=="78":
        tmp_week+="(7-8节)"

    student = Student.objects.filter(userid=request.user)
    student_grade = int(student[0].grade[0])+1

    ml = Course.objects.filter(course_week=tmp_week,course_grade=student_grade)

    #
    # if len(student) != 0:
    #     student = student[0]
    #     my_course = student.course_set.all().order_by('course_week')
    #     selected_course_weeks = [c.course_week for c in my_course]
    #     sumPrice = sum([c.course_price for c in my_course])

    return render_to_response('mooc_list.html', {'ml': ml})


@login_required
def mooc_detail(request, id):
    try:
        md = Course.objects.get(id=str(id))
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('mooc_detail.html', {'md': md})


@login_required
def course_add(request, id):
    student = Student.objects.filter(userid=request.user)
    course = Course.objects.get(id=id)
    dir = '/index/show'

    if len(student) != 0:
        #dir = '/mooc/' + id
        dir = '/index/show'
        student = student[0]
        verify_same_course = Course.objects.filter(course_name=course.course_name, course_choose=student)
        verify_same_time = Course.objects.filter(course_week=course.course_week, course_choose=student)

        if verify_same_course:
            messages.error(request, '您已选择学习此类课程, 每种课程一周只能选择一次课')
            return render_to_response('msg.html', {'messages': '对不起, 您已选择学习此类课程, 每种课程一周只能选择一次课'})
        elif verify_same_time:
            messages.error(request, '您已选择学习此时间段的课程, 请重新选择')
            return render_to_response('msg.html', {'messages': '对不起, 您已选择学习此时间段的课程, 请重新选择'})
        else:
            course.course_choose.add(student)
            course.save()
            messages.success(request, "恭喜你,你已选课成功")
            return render_to_response('msg.html', {'messages': "恭喜你,你已选课成功"})

    else:
        teacher = Teacher.objects.get(userid=request.user)
        verify = Course.objects.filter(id=id, course_teach=teacher)
        if verify:
            messages.error(request, '您已选择教授此课程')
        else:
            course.course_teach.add(teacher)
            course.save()
            messages.success(request, "选课成功")
    return HttpResponseRedirect(dir)


@login_required
def course_delete(request, id):
    student = Student.objects.filter(userid=request.user)
    course = Course.objects.get(id=id)
    dir = '/index/show'
    if len(student) != 0:
        student = student[0]
        verify = Course.objects.filter(id=id, course_choose=student)
        if not verify:
            messages.error(request, '您未选择学习此课程')
            return render_to_response('msg.html', {'messages': '对不起,您未选择学习此课程!'})
        else:
            course.course_choose.remove(student)
            course.save()
            messages.success(request, "你已经成功删除此课程")
            return render_to_response('msg.html', {'messages': "你已经成功删除此课程!"})
    else:
        teacher = Teacher.objects.get(userid=request.user)
        verify = Course.objects.filter(id=id, course_teach=teacher)

        if not verify:
            messages.error(request, '您未选择教授此课程')
        else:
            course.course_teach.remove(teacher)
            course.save()
            messages.success(request, "取消授课成功")
    return HttpResponseRedirect(dir)


@login_required
def show_scores(request):
    try:
        student = Student.objects.get(userid=request.user)
        scores = Score.objects.filter(student_id=student)
        return render(request, 'show_scores.html', {'my_scores': scores})
    except Student.DoesNotExist:
        return HttpResponse('只有学生可以操作')


@login_required
def show_my_course(request):
    student = Student.objects.filter(userid=request.user)

    if len(student) != 0:
        student = student[0]
        my_course = student.course_set.all().order_by('course_week')
        selected_course_weeks = [c.course_week for c in my_course]
        sumPrice = sum([c.course_price for c in my_course])
        return render(request, 'mooc_select_show.html', {'my_course': my_course, 'sumPrice': sumPrice,'selected_course_names':selected_course_weeks})
    else:
        teacher = Teacher.objects.get(userid=request.user)
        my_course = teacher.course_set.all().order_by('id')
        return render(request, 'teach_select_show.html', {'my_course': my_course})


@login_required
def show_who_choose_this_class(request, id):
    course = Course.objects.get(id=id)
    class_mates = course.course_choose.all()
    return render_to_response('mooc_class_mates.html', {'class_mates': class_mates})


@login_required
def set_scores(request, id):
    course = Course.objects.get(id=id)
    students = course.course_choose.all()
    stunum = len(students)
    ScoreFormSet = formset_factory(ScoreForm, extra=stunum)

    teacher = Teacher.objects.get(userid=request.user.id)

    if request.method == 'POST':
        formset = ScoreFormSet(request.POST)
        if formset.is_valid():
            cnt = 0
            for form in formset:
                if form.has_changed():

                    alscore = Score.objects.filter(student_id=students[cnt], teacher_id=teacher, course_id=course)
                    if alscore:
                        # 已有成绩
                        score = alscore[0]
                        score.value = form.cleaned_data['score']
                        score.save()
                    else:
                        # 新建成绩
                        score = Score(student_id=students[cnt], teacher_id=teacher, course_id=course,
                                      value=form.cleaned_data['score'])
                        score.save()
                    cnt += 1
            messages.success(request, '修改成绩成功')
        return HttpResponseRedirect('/index/show/')
    else:
        return render(request, 'set_scores.html', {'formset': ScoreFormSet(), 'students': students, 'id': id})


@login_required
def course1_intro(request):
    html = "<html><body>In %s hour(s), it will be %s.</body></html>"
    return HttpResponse(html)
