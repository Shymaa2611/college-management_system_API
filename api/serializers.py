from rest_framework import serializers
from .models import Course,Instructor,Mobile,Student,Grade,Attendance

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['course_name','course_score','student']

class instructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields='__all__'
class mobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobile
        fields='__all__'
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['user','first_name','last_name','student_age','student_address','student_level','department','course','GPA']
class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grade
        fields='__all__'
class attendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'