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
   # student=models.ForeignKey('Student',on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.course_name


class Mobile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    mobile_first_number=models.CharField(max_length=11,blank=True,null=True,verbose_name='First Number')
    mobile_second_number=models.CharField(max_length=11,blank=True,null=True,verbose_name='Second Number')
    def __str__(self):
        return self.mobile_first_number

class Instructor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=15,verbose_name='first name')
    last_name=models.CharField(max_length=15,verbose_name='last name')
    image=models.ImageField(upload_to='instructor/photo/',null=True,blank=True)
    material=models.FileField(upload_to='material/',blank=True,null=True)
    instructor_salary=models.DecimalField(verbose_name='salary',max_digits=5,decimal_places=1)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,verbose_name='mobile',related_name='instructor',blank=True,null=True)
    course=models.ManyToManyField(Course,related_name='instructor')
    def __str__(self):
        return str(self.first_name+' '+self.last_name)


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=15,verbose_name='first name')
    last_name=models.CharField(max_length=15,verbose_name='last name')
    image=models.ImageField(upload_to='student/photo/',null=True,blank=True)
    sheet=models.FileField(upload_to='tasks/',blank=True,null=True)
    student_age=models.IntegerField(default=0,verbose_name='age',blank=True,null=True)
    student_address=models.CharField(max_length=20,verbose_name='address',blank=True,null=True)
    student_level=models.CharField(max_length=1,choices=level,verbose_name='level')
    department=models.CharField(max_length=5,choices=department)
    #grade=models.IntegerField(default=0,blank=True,null=True)
    course=models.ManyToManyField(Course,related_name='student')
    GPA=models.FloatField(default=0)


    def __str__(self):
        return str(self.first_name+' '+self.last_name)

class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    attendance=models.CharField(max_length=20)
   

class Grade(models.Model):
   student=models.ForeignKey(Student,on_delete=models.CASCADE)
   Course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
   grade=models.DecimalField(max_digits=11,decimal_places=2)
   def __str__(self):
       return f'{self.student.first_name} {self.Course.course_name}'



def get_count():
    student=Student.objects.all()
    op=str(student.count())
    return op
   
    



