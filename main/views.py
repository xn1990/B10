# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django import forms
from models import User

class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
 
def index(request):
    username = request.COOKIES.get('cookie_username','')
    return render(request,'index.html',{'username':username})

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            op = request.POST['op']
            if op == "signin":
                #对比输入的用户名和密码和数据库中是否一致
                userPassJudge = User.objects.filter(username__exact=username,password__exact=password)
                if userPassJudge:
                    response = HttpResponseRedirect('/index.html')
                    response.set_cookie('cookie_username',username,3600)
                    return response
                else:
                    return HttpResponseRedirect('/login.html')
            else:
                User.objects.create(username= username,password=password)
                
    else:
        uf = UserForm(request.POST)
    return render(request,'login.html',{'uf':uf})

def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
    else:
        uf = UserForm()
    return render(request,'login.html',{'uf':uf})

def logout(request):
    #清理cookie里保存username
    response.delete_cookie('username')
    return render(request,'login.html')
