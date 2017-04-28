# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170428_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='First_name',
            field=models.CharField(max_length=20, null=True, verbose_name='\u59d3\u6c0f'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Last_name',
            field=models.CharField(max_length=20, null=True, verbose_name='\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True, verbose_name='\u6027\u522b'),
        ),
    ]
