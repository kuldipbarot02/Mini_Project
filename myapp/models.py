from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveBigIntegerField()
    remarks=models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveBigIntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
