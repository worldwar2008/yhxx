# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    # id = models.IntegerField(primary_key=True)
    name_zh = models.CharField(max_length=50)
    userid = models.OneToOneField(User, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender_choices = (
        (u'男', "男"),
        (u'女', "女"),
    )
    sex = models.CharField(max_length=50, choices=gender_choices, default=u'男')
    eduNumber = models.IntegerField(blank=True, null=True)
    socialNumber = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    study_stage = models.CharField(max_length=50, blank=True, null=True)
    campus = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    graduationdate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class TechChoose4Stu(models.Model):
    tech_userid = models.IntegerField(null=False)
    stu_userid = models.IntegerField(null=False)
    course_id = models.IntegerField(null=False)

    def __unicode__(self):
        return self.name


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name_zh', 'grade', 'class_name', 'study_stage']


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    userid = models.OneToOneField(User, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    socialNumber = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_choose = models.ManyToManyField(Student, blank=True)
    course_teach = models.ManyToManyField(Teacher, blank=True)
    course_grade = models.CharField(max_length=50, blank=True, null=True)
    course_year = models.CharField(max_length=50, blank=True, null=True)
    detail_weekTime_choice = (
        (u"周一(5-6节)", "周一(5-6节)"),
        (u"周一(7-8节)", "周一(7-8节)"),
        (u"周一(5-8节)", "周一(5-8节)"),
        (u"周二(5-6节)", "周二(5-6节)"),
        (u"周二(7-8节)", "周二(7-8节)"),
        (u"周二(5-8节)", "周二(5-8节)"),
        (u"周三(5-6节)", "周三(5-6节)"),
        (u"周三(7-8节)", "周三(7-8节)"),
        (u"周三(5-8节)", "周三(5-8节)"),
        (u"周四(5-6节)", "周四(5-6节)"),
        (u"周四(7-8节)", "周四(7-8节)"),
        (u"周四(5-8节)", "周四(5-8节)"),
        (u"周五️(5-6节)", "周五️(5-6节)"),
        (u"周五(7-8节)", "周五(7-8节)"),
        (u"周五(5-8节)", "周五(5-8节)")
    )
    course_week = models.CharField(max_length=50, choices=detail_weekTime_choice, default=u"周一(5-6节)")
    course_time = models.TimeField(blank=True, null=True)
    course_min_num = models.IntegerField(blank=True, null=True)
    course_max_num = models.IntegerField(blank=True, null=True)
    type_choice = (
        (u"高端", "高端"),
        (u"特色",  "特色"),
        (u"标准", "标准")
    )
    course_type = models.CharField(max_length=50, choices=type_choice, default=u"标准")
    course_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.course_name


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_type', 'course_week', 'course_year', 'course_grade', 'course_price']



ScoreChoice = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
    ('I', 'I'),
)


class Score(models.Model):
    student_id = models.ForeignKey('mooc.Student')
    teacher_id = models.ForeignKey('mooc.Teacher')
    course_id = models.ForeignKey('mooc.Course')
    value = models.CharField(max_length=3, choices=ScoreChoice)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'teacher_id', 'course_id', 'value']
    

class Notice(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    describe = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'describe']
