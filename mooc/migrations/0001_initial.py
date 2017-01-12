# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('course_grade', models.CharField(max_length=50, null=True, blank=True)),
                ('course_year', models.CharField(max_length=50, null=True, blank=True)),
                ('course_week', models.CharField(max_length=50, null=True, blank=True)),
                ('course_time', models.TimeField(null=True, blank=True)),
                ('course_min_num', models.IntegerField(null=True, blank=True)),
                ('course_max_num', models.IntegerField(null=True, blank=True)),
                ('course_type', models.CharField(max_length=50, null=True, blank=True)),
                ('course_price', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50, null=True)),
                ('describe', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=3, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F'), (b'I', b'I')])),
                ('course_id', models.ForeignKey(to='mooc.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('name_zh', models.CharField(max_length=50)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(max_length=50, null=True, blank=True)),
                ('eduNumber', models.IntegerField(null=True, blank=True)),
                ('socialNumber', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(max_length=50, null=True, blank=True)),
                ('study_stage', models.CharField(max_length=50, null=True, blank=True)),
                ('campus', models.CharField(max_length=50, null=True, blank=True)),
                ('grade', models.CharField(max_length=50, null=True, blank=True)),
                ('class_name', models.CharField(max_length=50, null=True, blank=True)),
                ('graduationdate', models.DateField(null=True, blank=True)),
                ('userid', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(max_length=50, null=True, blank=True)),
                ('socialNumber', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(max_length=50, null=True, blank=True)),
                ('department', models.CharField(max_length=50, null=True, blank=True)),
                ('userid', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TechChoose4Stu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tech_userid', models.IntegerField()),
                ('stu_userid', models.IntegerField()),
                ('course_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='student_id',
            field=models.ForeignKey(to='mooc.Student'),
        ),
        migrations.AddField(
            model_name='score',
            name='teacher_id',
            field=models.ForeignKey(to='mooc.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_choose',
            field=models.ManyToManyField(to='mooc.Student', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_teach',
            field=models.ManyToManyField(to='mooc.Teacher', blank=True),
        ),
    ]
