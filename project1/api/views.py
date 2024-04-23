from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
import io
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                data = StudentSerializer(stu)
                return JsonResponse(data)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)

        # If 'id' is not provided, retrieve all students
        stu = Student.objects.all()
        data = StudentSerializer(stu, many=True).data
        return JsonResponse(data, safe=False)  # Set safe=False for list of objects
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data) 
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': "created successfully!"
            }
            return JsonResponse(res)
        else:
            # If serializer is not valid, return the errors in the response
            return JsonResponse(serializer.errors, status=400)
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id =  python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = { 'msg':'Updated successfull!!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':'data deleted'})
        

# class based views

# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.permissions import AllowAny
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPIView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request, *args, **kwargs):
#         id = request.GET.get('id')
#         if id is not None:
#             try:
#                 stu = Student.objects.get(id=id)
#                 serializer = StudentSerializer(stu)
#                 return JsonResponse(serializer.data)
#             except Student.DoesNotExist:
#                 return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

#         # If 'id' is not provided, retrieve all students
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request, *args, **kwargs):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg': "created successfully!"}, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, *args, **kwargs):
#         id = request.data.get('id')
#         try:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'msg': 'Updated successfully!!'})
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Student.DoesNotExist:
#             return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, *args, **kwargs):
#         id = request.data.get('id')
#         try:
#             stu = Student.objects.get(id=id)
#             stu.delete()
#             return JsonResponse({'msg': 'Data deleted'})
#         except Student.DoesNotExist:
#             return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
