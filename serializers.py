from rest_framework import serializers
from .models import Category, Employees, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('Vendor', 'User')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'First_Name', 'Last_Name', 'Email', 'Password', 'Phone_Number')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_name', 'product_price', 'product_details', 'image')