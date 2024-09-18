from django.db import models 
from django.contrib.auth.models import User
# Create your models here.
class Category (models.Model):
    name =models.CharField(max_length=50)
    image =models.ImageField(upload_to='category_images',blank=True ,null=True)
    description =models.TextField(blank=True,null=True)


    
    class Meta:
        ordering =('name',)
        verbose_name_plural = 'Categories'  
        
    def __str__(self):
        return self.name
    
class Course (models.Model):
    category =models.ForeignKey(Category ,related_name='courses',on_delete=models.CASCADE)
    name =models.CharField(max_length=255)
    instructor =models.CharField(max_length=255)
    description =models.TextField(blank=True,null=True)
    duration =models.CharField(max_length=255)
    is_sold =models.BooleanField(default=False)
    price =models.FloatField()
    image =models.ImageField(upload_to='courses_images',blank=True ,null=True)
    created_by =models.ForeignKey(User ,related_name='courses' ,on_delete=models.CASCADE)
    createdAt =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class Student (models.Model):
    #Course =models.ForeignKey(Course ,related_name='students',on_delete=models.CASCADE)
    FulName =models.CharField(max_length=255)
    PhoneNumber =models.CharField(max_length=255)
    CourseName =models.TextField(blank=True,null=True)
    createdAt =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.FulName