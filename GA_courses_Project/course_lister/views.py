from django.shortcuts import render
from django.http import HttpResponse
from course_lister.models import Course

# Create your views here.


def index(request):
    course_list = Course.objects.all()
    context_dict = {}
    context_dict['course'] = course_list
    return render(request, 'course_lister/index.html', context=context_dict)
