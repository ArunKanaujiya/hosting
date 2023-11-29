from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(null=True,max_length=100)
    age=models.IntegerField(default=18)
    address=models.CharField(max_length=500,blank=True)
    image=models.FileField(null=True,blank=True)


Book_Choices= (
    ("COMIX", "comix"),
    ("LANGUAGE", "language"),
    ("NOWEL", "nowel"),
    ("REFRENCE","refrence"),
    ("HISTORICAL","historical")
)

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=100,
                       choices=Book_Choices,
                       default="nowel")

class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField( null=True,blank=True)
 
    
 
