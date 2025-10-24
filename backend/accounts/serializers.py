from rest_framework import serializers
from .models import Faculty, Student, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'phone_number']
        read_only_fields = ['id', 'username', 'user_type']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'user', 'enrollment_number', 'date_of_birth', 'gender', 'address',
            'branch', 'batch', 'father_name', 'father_phone', 'mother_name',
            'mother_phone', 'parent_email', 'guardian_name', 'guardian_phone', 'is_active'
        ]
        read_only_fields = ['user']


class FacultySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Faculty
        fields = ['user', 'employee_id', 'department', 'designation', 'date_of_joining', 'address', 'is_active']
        read_only_fields = ['user']
