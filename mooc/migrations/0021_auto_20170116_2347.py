# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0020_auto_20170116_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default=1, max_length=50, choices=[(0, '\u9ad8\u7aef'), (1, '\u7279\u8272'), (2, '\u6807\u51c6')]),
        ),
    ]
