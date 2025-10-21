from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet, FacultiesViewSet

router = DefaultRouter()
router.register(r'students', StudentsViewSet, basename='students')
router.register(r'faculties', FacultiesViewSet, basename='faculties')

urlpatterns = [
    path('', include(router.urls)),
]