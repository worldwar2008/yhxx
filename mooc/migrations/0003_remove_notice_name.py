# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_auto_20170112_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='name',
        ),
    ]
