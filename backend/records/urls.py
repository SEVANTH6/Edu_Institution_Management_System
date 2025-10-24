from django.urls import path
from . import views

urlpatterns = [
    # Fees URLs
    path('fees/', views.AllFeesRecordAPIView.as_view(), name='all_fees'),
    path('fees/<int:fee_id>/', views.OneFeesRecordAPIView.as_view(), name='one_fees'),

    # Marks URLs
    path('marks/', views.AllMarksAPIView.as_view(), name='all_marks'),
    path('marks/<int:marks_id>/', views.OneMarksAPIView.as_view(), name='one_marks'),

    # Backlogs URLs
    path('backlogs/', views.AllBacklogsAPIView.as_view(), name='all_backlogs'),
    path('backlogs/<int:backlog_id>/', views.OneBacklogsAPIView.as_view(), name='one_backlogs'),

    # Attendance URLs
    path('attendance/', views.AllAttendanceAPIView.as_view(), name='all_attendance'),
    path('attendance/<int:attendance_id>/', views.OneAttendanceAPIView.as_view(), name='one_attendance'),
]