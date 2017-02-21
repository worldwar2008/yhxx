# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0027_auto_20170119_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_grade',
            field=models.CharField(default=b'1', max_length=50, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')]),
        ),
    ]