from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Mark, Attendance
from .serializers import MarksSerializer, AttendanceSerializer

# Create your views here.

class MarksViewSet(viewsets.ModelViewSet):
    serializer_class = MarksSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        try:
            user = self.request.user 

            # Admin can see all marks
            if user.user_type == 'admin' or user.is_superuser:
                return Mark.objects.all()
            
            # Faculty can see all marks
            elif user.user_type == 'faculty':
                return Mark.objects.all()
            
            # Student can only see their own marks
            elif user.user_type == 'student':
                try:
                    return Mark.objects.filter(student__user=user) 
                except:
                    return Mark.objects.none()
            
            else:
                return Mark.objects.none()
                
        except Exception as e:
            print(e)
            return Mark.objects.none()

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        try:
            user = self.request.user
            
            # Admin can see all attendance
            if user.user_type == 'admin' or user.is_superuser:
                return Attendance.objects.all()
            
            # Faculty can see all attendance
            elif user.user_type == 'faculty':
                return Attendance.objects.all()
            
            # Student can only see their own attendance
            elif user.user_type == 'student':
                try:
                    return Attendance.objects.filter(student__user=user)
                except:
                    return Attendance.objects.none()
            
            else:
                return Attendance.objects.none()
                
        except Exception as e:
            print(e)
            return Attendance.objects.none()
