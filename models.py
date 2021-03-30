from django.db import models

# Create your models here.
class Category(models.Model):
    Vendor = models.CharField(max_length=20)
    User = models.CharField(max_length=20)



class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Email = models.EmailField()
    Password = models.CharField(max_length=10)
    Phone_Number = models.IntegerField()
    Role = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.First_Name

class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=100)
    Product_Price = models.FloatField()
    Product_Details = models.CharField(max_length=100,default="", null=True, blank=True)
    Image = models.ImageField(upload_to="image/download")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_Name

