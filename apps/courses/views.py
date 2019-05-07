from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Course
# Create your views here.


class CourseListView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        courses_all = Course.objects.all()
        return render(request, "course-list.html", {
            "courses_all": courses_all,
        })