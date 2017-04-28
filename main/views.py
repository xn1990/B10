# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib.auth.hashers import make_password, check_password
from django import forms
from models import User

class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

'''*********************************站点首页*********************************'''
 
def index(request):
    if request.session.get('session_username',False):
        username = request.session.get('session_username',False)
        img_url = User.objects.get(username__exact=username).headImg
        return render(request,'index.html',{'username':username,'img_url': img_url})
    else:
        return HttpResponseRedirect('/login')

'''*********************************登陆验证*********************************'''

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
                    request.session['session_username'] = username
                    response = HttpResponseRedirect('/')
                    return response
                else:
                    login_error = u'账号不存在或密码不正确'
            else:
                userPassJudge = User.objects.filter(username__exact=username)
                if userPassJudge:
                    regist_error = u'账号已存在'
                else:
                    password_length = len(password)
                    if ((password_length >= 8) & (password_length <=15)):
                        password = make_password(password,None,'pbkdf2_sha256')
                        User.objects.create(username= username,password= password)
                        return HttpResponseRedirect('/login#sign')
                    else:
                        regist_error = u'注册密码格式无效'
                
    else:
        uf = UserForm(request.POST)
        
    try:
        return render(request,'login.html',{'uf':uf, 'login_error':login_error, 'username':username})
    except:
        try:
            return render(request,'login.html',{'uf':uf, 'regist_error':regist_error})
        except:
            return render(request,'login.html',{'uf':uf})
        

def logout(request):
    try:
        del request.session['session_username']
    except KeyError:
        return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/login')

'''*********************************静态页面*********************************'''

def page_not_found(request):
    return render(request, 'page_404.html')


def page_error(request):
    return render(request, 'page_500.html')


def permission_denied(request):
    return render(request, 'page_403.html')

'''*********************************个人信息*********************************'''

def profile(request):
    if request.session.get('session_username',False):
        username = request.session.get('session_username',False)
        img_url = User.objects.get(username__exact=username).headImg
        return render(request,'profile.html',{'username':username,'img_url': img_url})
    else:
        return HttpResponseRedirect('/login')
