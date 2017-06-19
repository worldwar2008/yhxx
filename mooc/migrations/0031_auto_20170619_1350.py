# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0030_student_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_price1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_price2',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_price3',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='grade_can_choose',
            field=models.CharField(default=b'1', max_length=50, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')]),
        ),
    ]
