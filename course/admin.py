from django.contrib import admin
from .models import Category,Course,Student

admin.site.register(Category),
admin.site.register(Course)
admin.site.register(Student)