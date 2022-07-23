from django.contrib import admin

from .models import (Collage, Courses, Major, NoSemster, Semester,
                     SemsterCourses, Staff, Student)

# Register your models here.


class CollageAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_of_collage', 'manger_of_collage']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'collage', 'number_of_hour']


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_start', 'date_of_end']


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['collage', 'slug', 'semester', 'id_course']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'std_id', 'collage', 'major']


class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'staff_id', 'collage', 'fields', 'gender']


class NoSemsterAdmin(admin.ModelAdmin):
    list_display = ['slug', 'year', 'semster']


class SCoursesAdmin(admin.ModelAdmin):
    list_display = ['no_semster', 'instructor', 'coures']


admin.site.register(Collage, CollageAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(NoSemster, NoSemsterAdmin)
admin.site.register(SemsterCourses, SCoursesAdmin)
