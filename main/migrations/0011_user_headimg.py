# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_user_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='headImg',
            field=models.FileField(null=True, upload_to=b'static/upload/'),
        ),
    ]
