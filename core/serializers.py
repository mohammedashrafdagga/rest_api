from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Collage, Courses, Major, SemsterCourses, Staff, Student


class CollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = ('name', 'year_of_collage', 'date_of_created')


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('collage', 'name', 'number_of_hour', 'date_of_created')


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('collage', 'major', 'name', 'semester', 'year', 'id_course')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('std_id', 'user',
                  'std_image', 'collage', 'major')


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staff_id', 'user',
                  'staff_image', 'collage', 'fields')


class SemsterCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemsterCourses
        fields = ('slug', 'no_semster', 'semster',
                  'coures', 'instructor')
