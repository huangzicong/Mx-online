# _*_ coding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT


from users.views import ForgetPwdView, ResetView, ModifyPwdView, LoginView, RegisterView, ActiveUserView

urlpatterns = [
    # 后台管理系统
    url(r'^xadmin/', xadmin.site.urls),
    # 首页
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # 登陆页面
    url('^login/$', LoginView.as_view(), name="login"),
    # 注册页面
    url('^register/$', RegisterView.as_view(), name="register"),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),
    # 激活账户
    url(r'^active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),
    # 忘记密码
    url(r'^forget_pwd/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 重置密码
    url(r'^reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    # 修改密码
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构urls配置
    url(r'^org/', include('organization.urls', namespace="org")),
    # 课程urls配置
    url(r'^course/', include('courses.urls', namespace="course")),
    # 获取资源
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]
