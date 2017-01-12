# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0008_remove_notice_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notice',
            new_name='Notica',
        ),
    ]
