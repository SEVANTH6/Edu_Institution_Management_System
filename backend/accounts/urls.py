from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, FacultyViewSet, LogoutView, CustomAuthToken

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'faculties', FacultyViewSet, basename='faculties')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', CustomAuthToken.as_view(), name = 'login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]