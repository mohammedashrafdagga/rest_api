from django.urls import path

from .views import (collage_api, courses_api, courses_semster, major_api,
                    register, staff_api, students_api, test_view)

app_name = 'coreapp'

urlpatterns = [
    path('', test_view, name='home'),
    path('register', register, name='register'),
    path('api/collage/', collage_api, name='collage_api'),
    path('api/major/', major_api, name='major_api'),
    path('api/courses/', courses_api, name='courses_api'),
    path('api/student/', students_api, name='students_api'),
    path('api/staff/', staff_api, name='staff_api'),
    path('api/scourses/', courses_semster, name='courses_semster'),
]
