# _*_ coding: utf-8 _*_
from django.conf.urls import url, include


from .views import OrgView, UserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, OrgAddFavView

urlpatterns = [
    # 课程机构列表
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    # 用户添加我要学习
    url(r'^user_ask/$', UserAskView.as_view(), name="user_ask"),
    # 显示机构页面
    url(r'^org_home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    # 机构课程
    url(r'^org_course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    # 机构教师
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构详情
    url(r'^org_desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    # 用户添加收藏
    url(r'^add_fav/$', OrgAddFavView.as_view(), name="add_fav")
    # 课程
    # url(r'^course')


]
