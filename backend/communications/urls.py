from django.urls import path
from . import views

urlpatterns = [
    # Parent Alerts URLs
    path('alerts/', views.ParentAlertsAPIView.as_view(), name='parent_alerts'),
]