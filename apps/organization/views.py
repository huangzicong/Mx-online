# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from organization.models import CourseOrg, CityDict, Teacher
from operation.models import UserFavorite
from organization.forms import UserAskForm
# Create your views here.


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        org_all = CourseOrg.objects.all()
        city_all = CityDict.objects.all()
        # 取出热门组织
        hot_orgs = org_all.order_by('-click_nums')[:3]
        # 取出筛选城市
        city_id = request.GET.get("city", "")
        if city_id:
            org_all = org_all.filter(city_id=city_id)

        # 取出筛选类别
        category = request.GET.get("ct", "")
        if category:
            org_all = org_all.filter(category=category)

        # 排序方式
        sort = request.GET.get("sort", "")
        if sort:
            if sort == 'students':
                org_all = org_all.order_by("-students")
            elif sort == 'courses':
                org_all = org_all.order_by("-course_nums")
        org_nums = org_all.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(org_all, 5, request=request)
        orgs = p.page(page)
        return render(request, "org-list.html", {
            "org_all": orgs,
            "city_all": city_all,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
            "sort": sort,
        })


class UserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    """
    机构home页面
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=2):
                has_fav = True
        courses = course_org.course_set.all()[:3]
        teachers = course_org.teacher_set.all()[:2]
        current_page = 'home'
        return render(request, "org-detail-homepage.html", {
            "courses": courses,
            "teachers": teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgTeacherView(View):
    """
    机构教师页面
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=3):
                has_fav = True
        teachers = course_org.teacher_set.all()
        current_page = "teacher"
        return render(request, "org-detail-teachers.html", {
            "all_teachers": teachers,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgCourseView(View):
    """
    机构课程页面
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=1):
                has_fav = True
        courses = course_org.course_set.all()
        current_page = "course"
        return render(request, "org-detail-course.html", {
            "all_courses": courses,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgDescView(View):
    """
    机构详情页面
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        current_page = "desc"
        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page": current_page,
        })


class OrgAddFavView(View):
    """
    添加收藏
    """
    def post(self, request):
        fav_id = request.POST.get("fav_id", 0)
        fav_type = request.POST.get("fav_type", 0)
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exit_record = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exit_record:
            # 记录已经存在，则删除记录
            exit_record.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_favorite = UserFavorite()
            if int(fav_id) != 0 and int(fav_type != 0):
                user_favorite.user = request.user
                user_favorite.fav_id = int(fav_id)
                user_favorite.fav_type = int(fav_type)
                user_favorite.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')