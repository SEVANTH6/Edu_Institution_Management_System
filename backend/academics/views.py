from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Branches, Batches, Subjects, Classes, Class_sub
from .serializers import BranchesSerializer, BatchesSerializer, SubjectsSerializer, ClassesSerializer, Class_subSerializer

class BranchesView(viewsets.ModelViewSet):
    model = Branches
    queryset = model.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

class BatchesView(viewsets.ModelViewSet):
    model = Batches
    queryset = model.objects.all()
    serializer_class = BatchesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
class SubjectsView(viewsets.ModelViewSet):
    model = Subjects
    queryset = model.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
class ClassesView(viewsets.ModelViewSet):
    model = Classes
    queryset = model.objects.all()
    serializer_class = ClassesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
class Class_subView(viewsets.ModelViewSet):
    model = Class_sub
    queryset = model.objects.all()
    serializer_class = Class_subSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)