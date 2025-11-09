from rest_framework import viewsets
from .models import Student, Faculty
from .serializers import StudentSerializer, FacultySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Student ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        try:
            user = self.request.user 

            # if the user is admin, return all students
            if user.user_type == 'admin' or user.is_superuser:
                return Student.objects.all()
            # if the user is faculty, return students in their department
            elif user.user_type == 'faculty':
                try:   # get faculty profile
                    faculty = user.faculty_profile  #  Access Faculty from User (using related_name!)
                    return Student.objects.filter(branch=faculty.department)
                except Faculty.DoesNotExist:   # if faculty profile not found
                    return Student.objects.none()   
            # if user is student, return only their record
            elif user.user_type == 'student':
                try:  # get student profile
                    return Student.objects.filter(user=user)
                except Student.DoesNotExist:  # if student profile not found
                    return Student.objects.none()                  
            # if the user type is unknown, return no records
            else:
                return Student.objects.none() 
       
        except Exception as e:
            print(e)  # Log the error for debugging
            return Student.objects.none()

# Faculty ViewSet
class FacultyViewSet(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        try:
            user = self.request.user 
            # if the user is admin, return all faculties
            if user.user_type == 'admin' or user.is_superuser:
                return Faculty.objects.all()
            # if the user is faculty, return only their record
            elif user.user_type == 'faculty':
                return Faculty.objects.filter(user=user)
            # if user is student/others, return no records
            else:
                return Faculty.objects.none()
            
        except Exception as e:
            print(e)  # Log the error for debugging
            return Faculty.objects.none()