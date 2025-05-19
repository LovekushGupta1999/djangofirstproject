from django.db import models


class Admin(models.Model):
    Admin_name=models.CharField(max_length=50)
    Admin_email=models.EmailField()
    Admin_gender=models.CharField(max_length=50)
    Admin_image=models.ImageField(upload_to='images/', blank=True,null=True)
    Admin_document=models.FileField(upload_to='file/' , blank=True,null=True)
    Admin_password=models.CharField(max_length=50)

class Question(models.Model):
     ques=models.TextField(max_length=200)
     date=models.DateField()

     def __str__(self):
         return self.ques


class Student(models.Model):
    User_name=models.CharField(max_length=50)
    User_email=models.EmailField()
    User_gender=models.CharField(max_length=50)
    User_image=models.ImageField(upload_to='images/', blank=True,null=True)
    User_document=models.FileField(upload_to='file/' , blank=True,null=True)
    User_password=models.CharField(max_length=50)
    User_contact=models.IntegerField(blank=True,null=True)
    User_joindate=models.DateField(blank=True,null=True)
   
    
    def __str__(self):
        return f'Name:{self.User_name}, Email {self.User_email} '   
    
class Solution(models.Model):
    quest = models.ForeignKey('Question', on_delete=models.CASCADE)
    stu = models.ForeignKey('Student', on_delete=models.CASCADE)
    sol=models.TextField()
    feedback=models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.sol} of {self.quest.ques} by {self.stu.User_name}'
