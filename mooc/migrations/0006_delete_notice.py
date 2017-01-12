# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0005_notice_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
