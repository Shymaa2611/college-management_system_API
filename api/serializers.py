from rest_framework import serializers
from .models import Course,Instructor,Mobile,Student,Department

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
        fields='__all__'
class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'