
from django.urls import path

from .views import main

app_name = 'user_app'


urlpatterns = [
    path('', main, name='main'),

]
