# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0012_notice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default=b'man', max_length=50, choices=[(b'man', b'\xe7\x94\xb7'), (b'woman', b'\xe5\xa5\xb3')]),
        ),
    ]
