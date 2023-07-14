from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
import  rest_framework.status  as status
from .models import Course,Student,Instructor,Department,get_count
from .serializers import courseSerializer,studentSerializer,instructorSerializer,departmentSerializer
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
