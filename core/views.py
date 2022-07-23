from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (Collage, Courses, Major, Semester, SemsterCourses, Staff,
                     Student)
from .serializers import (CollageSerializer, CoursesSerializer,
                          MajorSerializer, SemsterCoursesSerializer,
                          StaffSerializer, StudentSerializer)

# Create your views here.


@login_required(login_url='/accounts/login/')
def test_view(request):
    user = User.objects.get(pk=request.user.id)
    std = Student.objects.get(user=user)
    return render(request, 'core/base.html', {'std': std, 'items': range(1, 10)})


@login_required(login_url='/accounts/login/')
def register(request):
    user = User.objects.get(pk=request.user.id)
    std = Student.objects.get(user=user)
    today = date.today()
    semster = Semester.objects.get(date_of_end__gte=today)
    courses = Courses.objects.filter(major=std.major, semester=semster)
    return render(request, 'core/register.html', {'courses': courses})


# Three View
@api_view(('GET',))
def collage_api(request):
    collage_get_all = Collage.objects.all()
    serializer = CollageSerializer(collage_get_all, many=True)
    return Response(serializer.data)

# Three View


@api_view(('GET', 'POST'))
def major_api(request):
    if request.method == 'GET':
        major_get_all = Major.objects.all()
        serializer = MajorSerializer(major_get_all, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MajorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Three View


@api_view(('GET',))
def courses_api(request):
    courses_get_all = Courses.objects.all()
    serializer = CoursesSerializer(courses_get_all, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def students_api(request):
    student_get_all = Student.objects.all()
    serializer = StudentSerializer(student_get_all, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def staff_api(request):
    staff_get_all = Staff.objects.all()
    serializer = StaffSerializer(staff_get_all,  many=True)
    return Response(serializer.data)


@api_view(('GET',))
def courses_semster(request):
    courses_semster_get_all = SemsterCourses.objects.all()
    serializer = SemsterCoursesSerializer(courses_semster_get_all, many=True)
    return Response(serializer.data)
