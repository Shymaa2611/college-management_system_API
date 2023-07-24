from django.contrib import admin
from .models import Course,Student,Instructor,Mobile,Grade,Attendance
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Mobile)
admin.site.register(Grade)
admin.site.register(Attendance)