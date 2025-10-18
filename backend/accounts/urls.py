from django.urls import path
from . import views

urlpatterns = [
    # Student URLs
    path("Student/", views.AllStudentAPIView.as_view(), name="student_api"),
    path("Student/<int:student_id>/", views.OneStudentAPIView.as_view(), name="one_student_api"),

    # Faculty URLs
    path("Faculty/", views.AllFacultyAPIView.as_view(), name="faculty_api"),
    path("Faculty/<int:faculty_id>/", views.OneFacultyAPIView.as_view(), name="one_faculty_api"),
]