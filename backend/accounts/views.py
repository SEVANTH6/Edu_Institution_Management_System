from rest_framework import viewsets
from .models import Student, Faculty
from .serializers import StudentSerializer, FacultySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


# Student ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter students based on user role.
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


# Faculty ViewSet
class FacultyViewSet(viewsets.ModelViewSet):
    # queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        # Filter faculties based on user role.
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


# Custom Auth Token 

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        # validate Username/Password
        serializer = self.serializer_class(data = request.data, context = {'request': request} )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # create or get token 
        token, created = Token.objects.get_or_create(user=user)

        # return token + user info
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'user_type': user.user_type
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete User Token to logout
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out.'})



# permission_classes = [IsAuthenticated] Because only authenticated users should access these endpoints