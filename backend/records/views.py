from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Mark, Attendance
from .serializers import MarksSerializer, AttendanceSerializer


# Create your views here.

class AllMarksAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
    
        if user.user_type == 'admin' or user.is_superuser:
            marks = Mark.objects.all()
        
        elif user.user_type == 'faculty':
            marks = Mark.objects.all()  
        
        elif user.user_type == 'student':
            try:
                marks = Mark.objects.filter(student__user=user)
            except:
                marks = Mark.objects.none()
        
        else:
            marks = Mark.objects.none()
        
        serializer = MarksSerializer(marks, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MarksSerializer(data = request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class OneMarksAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, marks_id):
        try:
            return Mark.objects.get(mark_id=marks_id)
        except Mark.DoesNotExist:
            return None
    
    def get(self, request, marks_id):
        mark = self.get_object(marks_id)
        if mark is None:
            return Response({'error': 'Mark not found'}, status=404)

        serializer = MarksSerializer(mark, context={'request': request})    
        return Response(serializer.data)

    def put(self, request, marks_id):
        mark = self.get_object(marks_id)
        if mark is None:
            return Response({'error': 'Mark not found'}, status=404)
        
        serializer = MarksSerializer(mark, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, marks_id):
        mark = self.get_object(marks_id)
        if mark is None:
            return Response({'error': 'Mark not found'}, status=404)
        mark.delete()
        return Response(status=204)
    

class AllAttendanceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        if user.user_type == 'admin' or user.is_superuser:
            attendance_records = Attendance.objects.all()
        
        elif user.user_type == 'faculty':
            attendance_records = Attendance.objects.all()  
        
        elif user.user_type == 'student':
            try:
                attendance_records = Attendance.objects.filter(student__user=user)
            except:
                attendance_records = Attendance.objects.none()
        
        else:
            attendance_records = Attendance.objects.none()
        
        serializer = AttendanceSerializer(attendance_records, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AttendanceSerializer(data = request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class OneAttendanceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, attendance_id):
        try:
            return Attendance.objects.get(attendance_id=attendance_id)
        except Attendance.DoesNotExist:
            return None

    def get(self, request, attendance_id):
        attendance_record = self.get_object(attendance_id)
        if attendance_record is None:
            return Response({'error': 'Attendance record not found'}, status=404)

        serializer = AttendanceSerializer(attendance_record, context={'request': request})    
        return Response(serializer.data)
    
    def put(self, request, attendance_id):
        attendance_record = self.get_object(attendance_id)
        if attendance_record is None:
            return Response({'error': 'Attendance record not found'}, status=404)
        
        serializer = AttendanceSerializer(attendance_record, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, attendance_id):
        attendance_record = self.get_object(attendance_id)
        if attendance_record is None:
            return Response({'error': 'Attendance record not found'}, status=404)
        
        attendance_record.delete()
        return Response(status=204)