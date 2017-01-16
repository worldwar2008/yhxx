# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0015_auto_20170116_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default=b'standard', max_length=50, choices=[(b'advanced', b'\xe9\xab\x98\xe7\xab\xaf'), (b'special', b'\xe7\x89\xb9\xe8\x89\xb2'), (b'standard', b'\xe6\xa0\x87\xe5\x87\x86')]),
        ),
    ]
