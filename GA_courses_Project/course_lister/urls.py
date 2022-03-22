from django.urls import path
from course_lister import views

app_name = 'course_lister'

urlpatterns = [
    path('', views.index, name='index')
]
