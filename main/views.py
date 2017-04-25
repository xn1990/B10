# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib.auth.hashers import make_password, check_password
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
                userPassJudge = User.objects.filter(username__exact=username)
                if userPassJudge:
                    db_password = User.objects.get(username__exact=username).password
                    userPassJudge = check_password(password,db_password)
                else:
                    login_error = u'账号不存在或密码不正确'
                if userPassJudge:
                    response = HttpResponseRedirect('/index.html')
                    response.set_cookie('cookie_username',username,3600)
                    return response
                else:
                    login_error = u'账号不存在或密码不正确'
            else:
                userPassJudge = User.objects.filter(username__exact=username)
                if userPassJudge:
                    regist_error = u'账号已存在'
                else:
                    password = make_password(password,None,'pbkdf2_sha256')
                    User.objects.create(username= username,password= password)
                    return HttpResponseRedirect('/login#signin')
                
    else:
        uf = UserForm(request.POST)
        
    if login_error & regist_error:
        return render(request,'login.html',{'uf':uf, 'login_error':login_error, 'regist_error':regist_error, 'username':username})

    if login_error:
        return render(request,'login.html',{'uf':uf, 'login_error':login_error, 'username':username})

    if regist_error:
        return render(request,'login.html',{'uf':uf, 'regist_error':regist_error})
        
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
