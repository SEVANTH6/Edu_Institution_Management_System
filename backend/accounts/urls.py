from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, FacultyViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students') # Create 6 endpoints for students automatically.
router.register(r'faculties', FacultyViewSet, basename='faculties') # Create 6 endpoints for faculties automatically.

urlpatterns = [
    path('', include(router.urls)),
]

