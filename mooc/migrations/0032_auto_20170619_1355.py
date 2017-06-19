# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0031_auto_20170619_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grade_can_choose',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
