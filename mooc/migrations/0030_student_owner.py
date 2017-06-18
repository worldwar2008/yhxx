# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0029_auto_20170119_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='owner',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
