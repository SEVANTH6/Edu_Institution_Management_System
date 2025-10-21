from rest_framework import viewsets
from .models import Students, Faculties
from .serializers import StudentsSerializer, FacultiesSerializer

# Create your views here.
class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class FacultiesViewSet(viewsets.ModelViewSet):
    queryset = Faculties.objects.all()
    serializer_class = FacultiesSerializer
    
