# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0021_auto_20170116_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default=b'2', max_length=50, choices=[(b'0', '\u9ad8\u7aef'), (b'1', '\u7279\u8272'), (b'2', '\u6807\u51c6')]),
        ),
    ]
