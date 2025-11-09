from rest_framework import serializers
from .models import Faculty, Student, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'phone_number']
        read_only_fields = ['id', 'username', 'user_type']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested Serializer - shows full user details in GET responses
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # Validates that user ID exists in database
        source='user',                 # Maps to the 'user' field in Student model
        write_only=True,               # Only for POST/PUT/PATCH, not shown in GET responses
        required=False                 # Optional - allows PATCH without sending user_id
    )
    class Meta:
        model = Student
        fields = [
            'user', 'user_id', 'enrollment_number', 'date_of_birth', 'gender', 'address',
            'branch', 'batch', 'father_name', 'father_phone', 'mother_name',
            'mother_phone', 'parent_email', 'guardian_name', 'guardian_phone', 'is_active'
        ]
        read_only_fields = ['user']

        
class FacultySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested Serializer - shows full user details in GET responses
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # Validates that user ID exists in database
        source='user',                 # Maps to the 'user' field in Faculty model
        write_only=True,               # Only for POST/PUT/PATCH, not shown in GET responses
        required=False                 # Optional - allows PATCH without sending user_id
    )
    class Meta:
        model = Faculty
        fields = ['user', 'user_id', 'employee_id', 'department', 'designation', 'date_of_joining', 'address', 'is_active']
        read_only_fields = ['user']
