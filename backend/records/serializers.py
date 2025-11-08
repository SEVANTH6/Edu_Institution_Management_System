from rest_framework import serializers
from .models import Mark, Attendance

class MarksSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    subject_name = serializers.CharField(source='subject.subject_name', read_only=True)

    class Meta:
        model = Mark 
        fields = [
            'mark_id', 'student', 'student_name', 'subject', 'subject_name',
            'exam_type', 'score', 'grade', 'created_at', 'modified_at',
            'modified_by', 'is_active'
        ]
        read_only_fields = ['mark_id', 'created_at', 'modified_at', 'modified_by']

    def validate_score(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Score must be between 0 and 100")
        return value
    
    def create(self, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super().update(instance, validated_data)


class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)

    class Meta:
        model = Attendance
        fields = [
            'attendance_id', 'student', 'student_name', 'date', 'status', 
            'class_sub', 'created_at', 'modified_at', 'modified_by', 'is_active'
        ]
        read_only_fields = ['attendance_id', 'created_at', 'modified_at', 'modified_by']
    
    def create(self, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super().update(instance, validated_data)