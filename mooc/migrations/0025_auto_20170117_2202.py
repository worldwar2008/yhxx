# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0024_auto_20170117_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default='\u7537', max_length=50, choices=[('\u7537', b'\xe7\x94\xb7'), ('\u5973', b'\xe5\xa5\xb3')]),
        ),
    ]
