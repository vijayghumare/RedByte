from django.contrib import admin
from .models import Products, Employees,Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductId', 'Product_Name', 'Product_Price', 'Product_Details', 'Image', 'category']
admin.site.register(Products,ProductAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmployeeId', 'First_Name', 'Last_Name', 'Email', 'Phone_Number']
admin.site.register(Employees,EmployeeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['User', 'Vendor']
admin.site.register(Category,CategoryAdmin)