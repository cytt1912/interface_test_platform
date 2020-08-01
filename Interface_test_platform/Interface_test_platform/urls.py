"""Interface_test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Platform.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('login/', login),
    path('login_action/',login_action),
    path('case_list/', caseList),
    url(r'^home/$', home),  # 进入首页
    url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),
    path('register/',register_login),
    url('account/login/',login)  #非登录状态需要先进入登录页面


]
