from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("Student/", views.StudentAPIView.as_view(), name="student_api"),
]