# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0016_auto_20170116_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default=b'standard', max_length=50, choices=[(b'advanced', '\u9ad8\u7aef'), (b'special', '\u7279\u8272'), (b'standard', '\u6807\u51c6')]),
        ),
    ]
