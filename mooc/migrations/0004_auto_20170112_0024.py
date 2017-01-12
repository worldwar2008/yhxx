# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0003_remove_notice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='describe',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='position',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
