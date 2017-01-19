# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0028_auto_20170119_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_week',
            field=models.CharField(default='\u5468\u4e00(5-6\u8282)', max_length=50, choices=[('\u5468\u4e00(5-6\u8282)', b'\xe5\x91\xa8\xe4\xb8\x80(5-6\xe8\x8a\x82)'), ('\u5468\u4e00(7-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x80(7-8\xe8\x8a\x82)'), ('\u5468\u4e00(5-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x80(5-8\xe8\x8a\x82)'), ('\u5468\u4e8c(5-6\u8282)', b'\xe5\x91\xa8\xe4\xba\x8c(5-6\xe8\x8a\x82)'), ('\u5468\u4e8c(7-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x8c(7-8\xe8\x8a\x82)'), ('\u5468\u4e8c(5-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x8c(5-8\xe8\x8a\x82)'), ('\u5468\u4e09(5-6\u8282)', b'\xe5\x91\xa8\xe4\xb8\x89(5-6\xe8\x8a\x82)'), ('\u5468\u4e09(7-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x89(7-8\xe8\x8a\x82)'), ('\u5468\u4e09(5-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x89(5-8\xe8\x8a\x82)'), ('\u5468\u56db(5-6\u8282)', b'\xe5\x91\xa8\xe5\x9b\x9b(5-6\xe8\x8a\x82)'), ('\u5468\u56db(7-8\u8282)', b'\xe5\x91\xa8\xe5\x9b\x9b(7-8\xe8\x8a\x82)'), ('\u5468\u56db(5-8\u8282)', b'\xe5\x91\xa8\xe5\x9b\x9b(5-8\xe8\x8a\x82)'), ('\u5468\u4e94(5-6\u8282)', b'\xe5\x91\xa8\xe4\xba\x94(5-6\xe8\x8a\x82)'), ('\u5468\u4e94(7-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x94(7-8\xe8\x8a\x82)'), ('\u5468\u4e94(5-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x94(5-8\xe8\x8a\x82)')]),
        ),
    ]
