from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# import
# Create your views here.
from Platform.models import *



@login_required
def welcome(request):
    # print("欢迎进入首页！")
    # return HttpResponse("欢迎进入首页！")
    return render(request, "welcome.html")


def login(request):
    return render(request, "login.html")


def caseList(request):
    return render(request,"caseList.html")

@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})

def child(request,eid,oid):
    res = child_json(eid)
    return render(request,eid,res)

def login_action(request):
    uname = request.GET['username']
    pword = request.GET['password']
    #auth库专门用来验证登录
    from django.contrib import auth
    #引入变量自定义实体user，auth函数在库里找到user时，返回user，否则返回None
    user = auth.authenticate(username=uname,password=pword)
    """
    同步表结构，生效表结构
    python3 manage.py makemigrations
    python3 manage.py migrate
    
    """
    if user is not None:
        """
         前端想给后端传数据，发送请求，如果不是表单提交，或者超链接。
         只用我们的异步接口请求(就是我们前面用的$.get("url",{参数}{返回动作函数}))的话，
         那么后端无论怎么写重定向语句，都是徒劳的，前端并不会直接跳转去/home/.

        """
        auth.login(request,user)
        request.session['user'] = uname
        return HttpResponse('成功')

    else:
        return HttpResponse('失败')

def register_login(request):
    uname = request.GET['username']
    pword = request.GET['password']
    #存到数据库中
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=uname,password=pword)
        user.save()
        return HttpResponse("注册成功！")
    except:
        return HttpResponse("注册失败！用户名已经存在了~")

#退出登录
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#吐槽
def pei(request):
    tc_text= request.GET['tc_text']
    print(tc_text)
    print('pei')
    DBComments.objects.create(user = request.user.username,text=tc_text)
    return HttpResponse('')

def api_help(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})

#控制不同的页面返回不同的数据：数据分发器
def child_json(eid):
    if eid == "home.html":
        data = DB_home_href.objects.all()
        res = {"hrefs":data}
        return res




