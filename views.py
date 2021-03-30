from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
#from django.http.responce import JsonResponce
from django.http import JsonResponse
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.files.storage import default_storage

from .models import Employees, Products
from .serializers import ProductSerializer, EmployeeSerializer, CategorySerializer

# Create your views here.
@csrf_exempt
def productApi(request,id=0):
    if request.method == 'GET': #GET is used for getting records from department table
        products = Products.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        #return JsonResponce(products_serializer.data, safe=False)#safe=false means we are telling to django is, we are fine if any prob in JSON data
        return HttpResponse(products_serializer.data, content_type="application/json", status=200)

    elif request.method== 'POST':
        product_data = JSONParser().parse(request)
        products_serializer = ProductSerializer(data=product_data) #serializer convert it into model type
        if products_serializer.is_valid():
            products_serializer.save()
            #return JsonResponce("Department added succesfully", safe=False)
            return HttpResponse(products_serializer.data,content_type="application/json", status=200)
        #return JsonResponce("Add to fail", safe=False)
        return HttpResponse(products_serializer.data,content_type="application/json", status=400)

    elif request.method == 'PUT': #for update record
        product_data = JSONParser().parse(request)
        product = Products.objects.get(ProductId=product_data['ProductId'])
        product_serializer = ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
        #return JsonResponce('Failed to Update', safe=False)
        return HttpResponse(product_serializer.data, content_type="application/json", status=200)

    elif request.method == 'DELETE':
        product = Products.objects.get(DepartmentId=id)
        product.delete()
        #return JsonResponce('Record deleted Succesfully', safe=False)
        return HttpResponse(product.data, content_type="application/json", status=200)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employee, many=True)
        #return JsonResponce(employees_serializer.data, safe=False)
        return HttpResponse(employees_serializer.data, content_type="application/json", status=200)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            #return JsonResponce("Record added succesfully", safe=False)
            return HttpResponse(employee_serializer.data, content_type="application/json", status=200)
        #return JsonResponce("Add to fail", safe=False)
        return HttpResponse(employee_serializer.data, content_type="application/json", status=400)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
        #return JsonResponce('Failed to Update', safe=False)
        return HttpResponse(employee_serializer.data, content_type="application/json", status=200)

    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        #return JsonResponce("Employee deleted succesfully", safe=False)
        return HttpResponse(employee.data, content_type="application/json", status=200)

