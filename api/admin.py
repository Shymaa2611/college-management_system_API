from django.contrib import admin
from .models import Course,Department,Student,Instructor,Mobile
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Department)
admin.site.register(Mobile)