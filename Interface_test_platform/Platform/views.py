from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# import
# Create your views here.

def welcome(request):
    # print("欢迎进入首页！")
    # return HttpResponse("欢迎进入首页！")
    return render(request, "welcome.html")


def login(request):
    return render(request, "login.html")


def caseList(request):
    return render(request,"caseList.html")

# def home(request):
#     return render(request,'welcome.html',{"whichHTML": "Home.html"})

def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})

def child(request,eid,oid):
    return render(request,eid)

def login_action(request):
    uname = request.GET['username']
    pword = request.GET['password']
    from django.contrib import auth
    user = auth.authenticate(username=uname,password=pword)
    if user is not None:
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponse('用户名或者密码错误！')


