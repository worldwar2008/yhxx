# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0025_auto_20170117_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.CharField(default='1\u73ed', max_length=50, choices=[('1\u73ed', b'1\xe7\x8f\xad'), ('2\u73ed', b'2\xe7\x8f\xad'), ('3\u73ed', b'3\xe7\x8f\xad'), ('4\u73ed', b'4\xe7\x8f\xad'), ('5\u73ed', b'5\xe7\x8f\xad'), ('6\u73ed', b'6\xe7\x8f\xad'), ('7\u73ed', b'7\xe7\x8f\xad'), ('8\u73ed', b'8\xe7\x8f\xad'), ('9\u73ed', b'9\xe7\x8f\xad'), ('10\u73ed', b'10\xe7\x8f\xad')]),
        ),
    ]
