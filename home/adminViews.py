from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from home.models import CustomUser, Staff, Courses
# from .forms import AddStudentForm, EditStudentForm


def admin_home(request):
    return render(request,"admin_template/home_content.html")

def add_staff(request):
    return render(request,"admin_template/add_staff_template.html")

def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        course = request.POST.get('course')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staff.course = course
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff/')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff/')

def add_course(request):
    return render(request, "admin_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        cn = request.POST.get('cname')
        cc = request.POST.get('code')
        sem = request.POST.get('sem')
        ay = request.POST.get('ay')
        minor = request.POST.get('minor')
        cred = request.POST.get('cred')
        try:
            course_model = Courses(course_code=cc,course_name=cn,sem=sem,academic_year=ay,minor=minor,credits=cred)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')
