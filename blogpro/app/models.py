from django.db import models


class User(models.Model):
    User_name=models.CharField(max_length=50)
    User_email=models.EmailField()
    User_gender=models.CharField(max_length=50)
    User_image=models.ImageField(upload_to='images/', blank=True)
    User_document=models.FileField(upload_to='file/' , blank=True)
    User_password=models.CharField(max_length=50)


class Student(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name    