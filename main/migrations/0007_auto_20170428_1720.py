# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170428_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1'),
        ),
    ]
