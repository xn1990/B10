# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(u'帐号',max_length=50)
    password = models.CharField(u'密码',max_length=200)

    First_name = models.CharField(u'姓氏',max_length=20,null = True)
    Last_name = models.CharField(u'名字',max_length=20,null = True)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(u'性别',max_length=2, choices=GENDER_CHOICES,null = True)

    email_address = models.EmailField(u'邮箱',null = True)

    IDENTITY_CHOICES = (
        (u'B', u'Boss'),
        (u'W', u'Worker'),
        (u'V', u'Volunteer'),
        (u'C', u'Cooperation'),
    )
    identity = models.CharField(u'身份',max_length=2, choices=IDENTITY_CHOICES,null = True)
    headImg = models.FileField(upload_to = 'static/upload/',null = True)
    
    creat_date = models.DateTimeField(u'创建时间', auto_now_add=True, editable = False)
    update_time = models.DateTimeField(u'修改时间',auto_now=True, null=True)

    def __unicode__(self):
        return self.username
