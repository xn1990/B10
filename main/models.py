# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(u'帐号',max_length=50)
    password = models.CharField(u'密码',max_length=200)

    Full_name = models.CharField(u'姓名',max_length=40,null = True)
    GENDER_CHOICES = (
        (u'男', u'男'),
        (u'女', u'女'),
    )
    gender = models.CharField(u'性别',max_length=2, choices=GENDER_CHOICES,null = True)
    living_address = models.CharField(u'住址',max_length=200,default='广东深圳')
    
    email_address = models.EmailField(u'邮箱',null = True,blank = True)

    IDENTITY_CHOICES = (
        (u'管理员', u'管理员'),
        (u'工作人员', u'工作人员'),
        (u'志愿者', u'志愿者'),
        (u'乐队', u'乐队'),
        (u'游客', u'游客'),
    )
    identity = models.CharField(u'身份',max_length=5, choices=IDENTITY_CHOICES,default = u'游客')
    headImg = models.FileField(upload_to = 'static/upload/',default = 'static/upload/default.jpg')
    
    creat_date = models.DateTimeField(u'创建时间', auto_now_add=True, editable = False)
    update_time = models.DateTimeField(u'修改时间',auto_now=True, null=True)

    def __unicode__(self):
        return self.username
