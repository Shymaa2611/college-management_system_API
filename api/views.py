from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
import  rest_framework.status  as status
from .models import Course,Student,Instructor,get_count,Attendance
from .serializers import courseSerializer,studentSerializer,instructorSerializer,attendenceSerializer
from django.http import HttpResponse, FileResponse
from django.http import FileResponse
from reportlab.pdfgen import canvas

@api_view(['GET','POST'])
def student_data(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer = studentSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = studentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def change_data(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = studentSerializer(student)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = studentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        student.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def search_student_GPA(request):
     data = Student.objects.filter(
        student_GPA=request.data['student_GPA'],
    )
     serializer=studentSerializer(data,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def get_ten_first_student(request):
    student=Student.objects.all()
    op=student.order_by('-student_GPA')[:10]
    serializer = studentSerializer(op, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def get_data(request):
   data=get_count()
   json={
       "number of student in college is ":data
   }
   return Response(json,status=status.HTTP_200_OK)

@api_view(['POST'])
def enroll_subject(request):
    newStudent=Student()
    newStudent.first_name=request.data['first_name']
    newStudent.last_name=request.data['last_name']
    newStudent.student_level=request.data['student_level']
    newStudent.course= Course.objects.get(id=request.data['course_id'])
    new_enroll=Student.objects.create(first_name= newStudent.first_name,last_name=newStudent.last_name,student_level= newStudent.student_level,department= newStudent.department,course= newStudent.course)
    new_enroll.save()
    json={
        "message":"successfully encrolling in course "
    }
    return Response(json,status=status.HTTP_201_CREATED)
@api_view(['POST'])

def generate_report(request,pk):
    student = Student.objects.get(pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.first_name}_report.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 750, f'Student Report for {student.first_name}')
    p.drawString(100, 700, f'Grade: {student.grade}')
    p.drawString(100, 650, f'Attendance: {student.attendance}')
    p.showPage()
    p.save()
    response = FileResponse(open(f'{student.first_name}_report.pdf', 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.first_name}_report.pdf"'
    return response

@api_view(['GET','POST'])
def student_attendeance(request, pk):

    if 'attendance' in request.data:
            student= Student.objects.get(pk=pk)
            course_name= request.data['course_name']
            attendance= request.data['attendance']
            first_name = request.data['first_name']
            user =Instructor.objects.get(first_name=first_name)
            course =Course.objects.get(course_name=course_name)
            try:
                attend= Attendance.objects.get(instructor=user, student=student.pk,course=course) 
                attend.attendance =attendance
                attend.save()
                serializer =attendenceSerializer(attend,many=False)
                json = {
                    'message': 'attendance of studentis Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                attend = Attendance.objects.create(attendance=attendance, student=student,course=course ,instructor=user)
                serializer=attendenceSerializer(attend, many=False)
                json = {
                    'message': 'student attendance is Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

    else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)
