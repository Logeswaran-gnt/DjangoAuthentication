# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from modelsapp.models import Post
from modelsapp.models import student
from django.conf import settings

@login_required
def index(request):
        all_entries = Post.objects.filter(title="python")
        #all_entries = Post.objects.all()
        #data = serializers.serialize("json", all_entries)
        #ins=student(name="Logeswaran",address="Madurai")
        #ins.save()
        wstdata=student.objects.filter(name='xyz').update(name="Lokace")
        #stdata.save()
        #for item in stdata:
        #        item.save()
        #rstdata=student.objects.all()
        #data = serializers.serialize("json", rstdata)
        rawquery=[]
        for i in student.objects.raw("select * from modelsapp_student"):
                rawquery.append(i)
        data = serializers.serialize("json", rawquery)
        return HttpResponse(data)

def login_view(request):
        print("==============================")
        print(request.user, request.user.is_authenticated)
        print("==========================")
        if request.user.is_authenticated:
                return redirect('/homepage')
        else:
                return render (request,'modelsapp/login.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print (user)
        #history(request)
        return redirect('/homepage')
        #return render(request, 'ServerAccess/history.html')
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def logout_view(request):
    logout(request)
    return redirect('/')