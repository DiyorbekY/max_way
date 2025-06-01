# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField()
    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    cost=models.IntegerField(null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    image=models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Customer(models.Model):
    first_name=models.CharField(max_length=100,null=False,blank=False)
    last_name=models.CharField(max_length=100,null=False,blank=False)
    phone_number=models.CharField(max_length=100,unique=True,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    payment_type=models.IntegerField(null=False,blank=False)
    status=models.CharField(max_length=255,null=True,blank=True,default=1)
    address=models.CharField(max_length=255,null=False,blank=False)
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.customer

class OrderProduct(models.Model):
    count=models.IntegerField(null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.product