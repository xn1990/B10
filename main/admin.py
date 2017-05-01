# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('Full_name','gender','identity')

admin.site.register(User,UserAdmin)
