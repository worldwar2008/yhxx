# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0009_auto_20170112_0943'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notica',
        ),
    ]
