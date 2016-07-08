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
    sex = models.CharField(max_length=50, blank=True, null=True)
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


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']


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
    course_week = models.CharField(max_length=50, blank=True, null=True)
    course_time = models.TimeField(blank=True, null=True)
    course_min_num = models.IntegerField(blank=True, null=True)
    course_max_num = models.IntegerField(blank=True, null=True)
    course_type = models.CharField(max_length=50, blank=True, null=True)
    course_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.course_name


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name']


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
