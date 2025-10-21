from rest_framework import serializers
from .models import Students, Faculties

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = '__all__'


