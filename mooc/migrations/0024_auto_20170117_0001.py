# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0023_auto_20170116_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default='\u6807\u51c6', max_length=50, choices=[('\u9ad8\u7aef', b'\xe9\xab\x98\xe7\xab\xaf'), ('\u7279\u8272', b'\xe7\x89\xb9\xe8\x89\xb2'), ('\u6807\u51c6', b'\xe6\xa0\x87\xe5\x87\x86')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_week',
            field=models.CharField(default='\u5468\u4e00(5-6\u8282)', max_length=50, choices=[('\u5468\u4e00(5-6\u8282)', b'\xe5\x91\xa8\xe4\xb8\x80(5-6\xe8\x8a\x82)'), ('\u5468\u4e00(7-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x80(7-8\xe8\x8a\x82)'), ('\u5468\u4e00(5-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x80(5-8\xe8\x8a\x82)'), ('\u5468\u4e8c(5-6\u8282)', b'\xe5\x91\xa8\xe4\xba\x8c(5-6\xe8\x8a\x82)'), ('\u5468\u4e8c(7-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x8c(7-8\xe8\x8a\x82)'), ('\u5468\u4e8c(5-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x8c(5-8\xe8\x8a\x82)'), ('\u5468\u4e09(5-6\u8282)', b'\xe5\x91\xa8\xe4\xb8\x89(5-6\xe8\x8a\x82)'), ('\u5468\u4e09(7-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x89(7-8\xe8\x8a\x82)'), ('\u5468\u4e09(5-8\u8282)', b'\xe5\x91\xa8\xe4\xb8\x89(5-8\xe8\x8a\x82)'), ('\u5468\u56db(5-6\u8282)', b'\xe5\x91\xa8\xe5\x9b\x9b(5-6\xe8\x8a\x82)'), ('\u5468\u56db(7-8\u8282)', b'\xe5\x91\xa8\xe5\x9b\x9b(7-8\xe8\x8a\x82)'), ('\u5468\u56db(5-8\u8282)', b'\xe5\x91\xa8\xe5\x9b\x9b(5-8\xe8\x8a\x82)'), ('\u5468\u4e94\ufe0f(5-6\u8282)', b'\xe5\x91\xa8\xe4\xba\x94\xef\xb8\x8f(5-6\xe8\x8a\x82)'), ('\u5468\u4e94(7-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x94(7-8\xe8\x8a\x82)'), ('\u5468\u4e94(5-8\u8282)', b'\xe5\x91\xa8\xe4\xba\x94(5-8\xe8\x8a\x82)')]),
        ),
    ]
