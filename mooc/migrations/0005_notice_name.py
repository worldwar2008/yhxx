# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0004_auto_20170112_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
