from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarksViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'marks', MarksViewSet, basename='marks')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
]