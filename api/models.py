from django.db import models
from django.contrib.auth.models import User

department={
    ("IS","IS"),
    ("CS","CS"),
    ("BIO","BIO"),
    ("None","None"),
}
level={
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4")
}
class Course(models.Model):
    course_name=models.CharField(max_length=20,blank=True,null=True,verbose_name='course')
    course_score=models.IntegerField(default=0,verbose_name='score')
    def __str__(self):
        return self.course_name


class Mobile(models.Model):
    mobile_first_number=models.CharField(max_length=11,blank=True,null=True,verbose_name='First Number')
    mobile_second_number=models.CharField(max_length=11,blank=True,null=True,verbose_name='Second Number')
    def __str__(self):
        return self.mobile_first_number


class Instructor(models.Model):
    first_name=models.CharField(max_length=15,verbose_name='first name')
    last_name=models.CharField(max_length=15,verbose_name='last name')
    instructor_salary=models.DecimalField(verbose_name='salary',max_digits=5,decimal_places=1)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,verbose_name='mobile',related_name='instructor',blank=True,null=True)
    course=models.ManyToManyField(Course,related_name='instructor')
    def __str__(self):
        return str(self.first_name+' '+self.last_name)

class Department(models.Model):
    department_name=models.CharField(choices=department,max_length=10,verbose_name='department')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='department',blank=True,null=True)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='department',blank=True,null=True)
    def __str__(self):
        return self.department_name
		
		


class Student(models.Model):
    first_name=models.CharField(max_length=15,verbose_name='first name')
    last_name=models.CharField(max_length=15,verbose_name='last name')
    student_age=models.IntegerField(default=0,verbose_name='age')
    student_address=models.CharField(max_length=20,verbose_name='address')
    student_mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,related_name='student',blank=True,null=True)
    student_GPA=models.DecimalField(max_digits=3,decimal_places=2)
    student_level=models.CharField(max_length=1,choices=level,verbose_name='level')
    department=models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name='department',related_name='student',blank=True,null=True)
    cousre=models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.first_name+' '+self.last_name)
def get_count():
    student=Student.objects.all()
    op=str(student.count())
    return op
   
    



