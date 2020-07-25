from django.http import HttpResponse
from django.shortcuts import render


# import
# Create your views here.

def welcome(request):
    # print("欢迎进入首页！")
    # return HttpResponse("欢迎进入首页！")
    return render(request, "welcome.html")


def caseList(request):
    return render(request,"caseList.html")

# def home(request):
#     return render(request,'welcome.html',{"whichHTML": "Home.html"})

def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})

def child(request,eid,oid):
    return render(request,eid)

