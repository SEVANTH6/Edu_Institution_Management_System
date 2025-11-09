from rest_framework import serializers
from .models import Branches, Batches, Subjects, Classes, Class_sub


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'
        read_only_fields = ('branch_id', 'created_at', 'modified_at')


class BatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = '__all__'
        read_only_fields = ('batch_id', 'created_at', 'modified_at')


class SubjectsSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.branch_name', read_only=True)
    
    class Meta:
        model = Subjects
        fields = '__all__'
        read_only_fields = ('subject_id', 'created_at', 'modified_at')


class ClassesSerializer(serializers.ModelSerializer):
    class_teacher_name = serializers.SerializerMethodField()
    batch_name = serializers.CharField(source='batch.batch_name', read_only=True)
    students_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Classes
        fields = '__all__'
        read_only_fields = ('class_id', 'created_at', 'modified_at')
    
    def get_class_teacher_name(self, obj):
        if obj.class_teacher and obj.class_teacher.user:
            return obj.class_teacher.user.get_full_name()
        return None
    
    def get_students_count(self, obj):
        return obj.students.count() if obj.students else 0


class Class_subSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject_name', read_only=True)
    class_name = serializers.CharField(source='class_id.class_name', read_only=True)
    faculty_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Class_sub
        fields = '__all__'
        read_only_fields = ('class_sub_id', 'created_at', 'modified_at')
    
    def get_faculty_name(self, obj):
        if obj.faculty and obj.faculty.user:
            return obj.faculty.user.get_full_name()
        return None