# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from mooc.models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from forms import *
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.


@login_required
def mooc_list(request, course_time):
    tmp_time = str(course_time)
    tmp_week = ""

    if tmp_time[0] == "1":
        tmp_week += "周一"
    elif tmp_time[0] == "2":
        tmp_week += "周二"
    elif tmp_time[0] == "3":
        tmp_week += "周三"
    elif tmp_time[0] == "4":
        tmp_week += "周四"
    elif tmp_time[0] == "5":
        tmp_week += "周五"

    long_tmp_week = ""
    if int(tmp_time[1])==5:
        long_tmp_week += tmp_week + "(5-8节)"
    if int(tmp_time[-1]) == 8:
        long_tmp_week += tmp_week + "(5-8节)"



    if tmp_time[1:] == "56":
        tmp_week += "(5-6节)"
    elif tmp_time[1:] == "78":
        tmp_week += "(7-8节)"


    student = Student.objects.filter(userid=request.user)
    student_grade = int(student[0].grade[0]) + 1

    ml = Course.objects.filter(course_week=tmp_week, course_grade=student_grade).order_by('course_type')

    long_ml = Course.objects.filter(course_week=long_tmp_week, course_grade=student_grade).order_by('course_type')


    #
    # if len(student) != 0:
    #     student = student[0]
    #     my_course = student.course_set.all().order_by('course_week')
    #     selected_course_weeks = [c.course_week for c in my_course]
    #     sumPrice = sum([c.course_price for c in my_course])
    if len(long_ml) == 0:

        return render_to_response('mooc_list.html', {'ml': ml})
    else:
        return render_to_response('mooc_list.html', {'ml': ml, 'long_ml': long_ml})


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

    gd_st = "2016-07-08 15:00:00"
    gd_et = "2016-07-10 14:00:00"

    ts_st = "2016-07-09 10:00:00"
    ts_et = "2016-07-10 14:00:00"

    bz_st = "2016-07-10 19:00:00"
    bz_et = "2016-07-11 20:00:00"

    if len(student) != 0:
        # dir = '/mooc/' + id
        dir = '/index/show'
        student = student[0]
        verify_same_course = Course.objects.filter(course_name=course.course_name, course_choose=student)
        verify_same_time = Course.objects.filter(course_week=course.course_week, course_choose=student)
        tmp_week = course.course_week

        verify_tese_class_num = Course.objects.filter(course_type=u"特色", course_choose=student).count()


        if verify_tese_class_num >= 3:
            return render_to_response('msg.html', {'messages': '对不起, 您选择的特色课程数目已经超过3个, 不能再多选'})



        if int(tmp_week.split("-")[1][0]):
            long_week = tmp_week.split("(")[0]+u"(5-8节)"
            verify_long_course = Course.objects.filter(course_week=long_week, course_choose=student)
            if verify_long_course:
                return render_to_response('msg.html', {'messages': '对不起, 您已选此时间段的课程, 请重新选择'})

        if int(tmp_week.split("-")[1][0]) == 8:
            long_week = tmp_week.split("(")[0]+u"(7-8节)"

            verify_long_course = Course.objects.filter(course_week=long_week, course_choose=student)
            if verify_long_course:
                return render_to_response('msg.html', {'messages': '对不起, 您已选此时间段的课程, 请重新选择'})

        now_time = datetime.now()

        gd_s = datetime.strptime(gd_st,"%Y-%m-%d %H:%M:%S")
        gd_e = datetime.strptime(gd_et,"%Y-%m-%d %H:%M:%S")

        ts_s = datetime.strptime(ts_st,"%Y-%m-%d %H:%M:%S")
        ts_e = datetime.strptime(ts_et,"%Y-%m-%d %H:%M:%S")

        bz_s = datetime.strptime(bz_st,"%Y-%m-%d %H:%M:%S")
        bz_e = datetime.strptime(bz_et,"%Y-%m-%d %H:%M:%S")

        if course.course_type[0] == u"高":
            if now_time < gd_s:
                return render_to_response('msg.html', {'messages': '对不起, 高端选课还没开始'})

        if course.course_type[0] == u"高":
            if now_time > gd_e:
                return render_to_response('msg.html', {'messages': '对不起, 高端选课已经结束'})

        if course.course_type == u"特色":
            if now_time < ts_s:
                return render_to_response('msg.html', {'messages': '对不起, 特色选课还没开始'})

        if course.course_type == u"特色":
            if now_time > ts_e:
                return render_to_response('msg.html', {'messages': '对不起, 特色选课已经结束'})

        if course.course_type == u"标准":
            if now_time < bz_s:
                return render_to_response('msg.html', {'messages': '对不起, 标准选课还没开始'})

        if course.course_type == u"标准":
            if now_time > bz_e:
                return render_to_response('msg.html', {'messages': '对不起, 标准选课已经结束'})

        # course max num limit

        course_max_num = course.course_max_num
        course_now_num = course.course_choose.count()

        if verify_same_course:
            messages.error(request, '您已选择学习此类课程, 每种课程一周只能选择一次课')
            return render_to_response('msg.html', {'messages': '对不起, 您已选择学习此类课程, 每种课程一周只能选择一次课'})
        elif verify_same_time:
            messages.error(request, '您已选择学习此时间段的课程, 请重新选择')
            return render_to_response('msg.html', {'messages': '对不起, 您已选择学习此时间段的课程, 请重新选择'})
        elif course_now_num >= course_max_num:
            return render_to_response('msg.html', {'messages': '对不起, 这门课的选课人数已经超过限制, 请您选修其他课程'})
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

    gd_st = "2016-07-08 15:00:00"
    gd_et = "2016-07-10 09:30:00"

    ts_st = "2016-07-09 10:00:00"
    ts_et = "2016-07-10 14:00:00"

    bz_st = "2016-07-10 19:00:00"
    bz_et = "2016-07-11 20:00:00"

    if len(student) != 0:
        student = student[0]
        verify = Course.objects.filter(id=id, course_choose=student)

        course_max_num = course.course_max_num
        course_min_num = course.course_min_num
        course_now_num = course.course_choose.count()

        now_time = datetime.now()

        gd_s = datetime.strptime(gd_st,"%Y-%m-%d %H:%M:%S")
        gd_e = datetime.strptime(gd_et,"%Y-%m-%d %H:%M:%S")

        ts_s = datetime.strptime(ts_st,"%Y-%m-%d %H:%M:%S")
        ts_e = datetime.strptime(ts_et,"%Y-%m-%d %H:%M:%S")

        bz_s = datetime.strptime(bz_st,"%Y-%m-%d %H:%M:%S")
        bz_e = datetime.strptime(bz_et,"%Y-%m-%d %H:%M:%S")

        if course.course_type[0] == u"高":
            if now_time > gd_e:
                return render_to_response('msg.html', {'messages': '对不起, 高端课程选课已经结束, 你无法进行相关操作'})
        if course.course_type[0] == u"特":
            if now_time > ts_e:
                return render_to_response('msg.html', {'messages': '对不起, 特色课程选课已经结束, 你无法进行相关操作'})
        if course.course_type[0] == u"标":
            if now_time > bz_e:
                return render_to_response('msg.html', {'messages': '对不起, 特色课程选课已经结束, 你无法进行相关操作'})



        if not verify:
            messages.error(request, '您未选择学习此课程')
            return render_to_response('msg.html', {'messages': '对不起,您未选择学习此课程!'})
        elif course_now_num >= course_max_num:
            return render_to_response('msg.html', {'messages': '对不起, 当前已满足开班人数的课程, 不能退选'})
        elif course_now_num >= course_min_num:
            return render_to_response('msg.html', {'messages': '对不起, 当前课程已经满足开课的最小人数, 无法删除'})


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
        selected_course_names = [c.course_name for c in my_course]
        student_name = student.name_zh
        formated_course_56 = []
        formated_course_78 = []

        if int(student.grade[0])+1 == 3:


            if u"周一(5-6节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(5-6节)" in item :
                        formated_course_56.append(selected_course_names[index])

            elif u"周一(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(5-8节)" in item :
                        formated_course_56.append(selected_course_names[index])

            else:
                formated_course_56.append("待选")

            if u"周一(7-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])
            elif u"周一(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(5-8节)" in item :
                        formated_course_78.append(selected_course_names[index])

            else:
                formated_course_78.append("待选")

            # 周二 u
            formated_course_56.append("实践")
            formated_course_78.append("实践")

            if u"周三(5-6节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周三(5-6节)" in item :
                        formated_course_56.append(selected_course_names[index])

            elif u"周三(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周三(5-8节)" in item :
                        formated_course_56.append(selected_course_names[index])

            else:
                formated_course_56.append("待选")

            if u"周三(7-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周三(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])

            elif u"周三(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周三(5-8节)" in item :
                        formated_course_78.append(selected_course_names[index])

            else:
                formated_course_78.append("待选")


            if u"周四(5-6节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(5-6节)" in item :
                        formated_course_56.append(selected_course_names[index])

            elif u"周四(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(5-8节)" in item :
                        formated_course_56.append(selected_course_names[index])

            else:
                formated_course_56.append("待选")

            if u"周四(7-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])

            elif u"周四(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])
            else:
                formated_course_78.append("待选")


            formated_course_56.append("班队会")
            formated_course_78.append("班队会")

        elif int(student.grade[0])+1 == 5:


            if u"周一(5-6节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(5-6节)" in item :
                        formated_course_56.append(selected_course_names[index])

            elif u"周一(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(5-8节)" in item :
                        formated_course_56.append(selected_course_names[index])

            else:
                formated_course_56.append("待选")

            if u"周一(7-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])

            elif u"周一(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周一(5-8节)" in item :
                        formated_course_78.append(selected_course_names[index])
            else:
                formated_course_78.append("待选")


            if u"周二(5-6节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周二(5-6节)" in item :
                        formated_course_56.append(selected_course_names[index])

            elif u"周二(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周二(5-8节)" in item :
                        formated_course_56.append(selected_course_names[index])
            else:
                formated_course_56.append("待选")

            if u"周二(7-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周二(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])
            elif u"周二(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周二(5-8节)" in item :
                        formated_course_78.append(selected_course_names[index])
            else:
                formated_course_78.append("待选")
            # 周二 u
            formated_course_56.append("实践")
            formated_course_78.append("实践")



            if u"周四(5-6节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(5-6节)" in item :
                        formated_course_56.append(selected_course_names[index])

            elif u"周四(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(5-8节)" in item :
                        formated_course_56.append(selected_course_names[index])

            else:
                formated_course_56.append("待选")

            if u"周四(7-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(7-8节)" in item :
                        formated_course_78.append(selected_course_names[index])

            elif u"周四(5-8节)" in selected_course_weeks:
                for index, item in enumerate(selected_course_weeks):
                    if u"周四(5-8节)" in item :
                        formated_course_78.append(selected_course_names[index])
            else:
                formated_course_78.append("待选")


            formated_course_56.append("班队会")
            formated_course_78.append("班队会")

        formated_course_56.reverse()
        formated_course_78.reverse()
        print "formated_course_56", formated_course_56
        print "formated_course_78", formated_course_78


        return render(request, 'mooc_select_show.html',
                      {'my_course': my_course, 'sumPrice': sumPrice, 'selected_course_names': selected_course_weeks,
                       'student_name':student_name, 'formated_course_56': formated_course_56,
                       'formated_course_78': formated_course_78, 'student_grade':int(student.grade[0])+1})
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
