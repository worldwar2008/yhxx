# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0026_auto_20170118_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default='\u6807\u51c6', max_length=50, choices=[('\u9ad8\u7aef', b'\xe9\xab\x98\xe7\xab\xaf'), ('\u7279\u8272', b'\xe7\x89\xb9\xe8\x89\xb2'), ('\u6807\u51c6', b'\xe6\xa0\x87\xe5\x87\x86'), ('\u5fc5\u9009', b'\xe5\xbf\x85\xe9\x80\x89')]),
        ),
    ]
