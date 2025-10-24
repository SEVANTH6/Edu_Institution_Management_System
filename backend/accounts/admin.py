from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Faculty, Student

# Register User model
admin.site.register(User, UserAdmin)

# Register Faculty and Student
admin.site.register(Faculty)
admin.site.register(Student)