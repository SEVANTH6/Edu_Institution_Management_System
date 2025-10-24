from rest_framework import serializers
from .models import *

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'

class BatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = '__all__'

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class ClassSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_sub
        fields = '__all__'

