# communication/models.py
from django.db import models
from django.utils import timezone

class AlertStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    SENT = 'Sent', 'Sent'
    READ = 'Read', 'Read'
    FAILED = 'Failed', 'Failed'

class ParentAlerts(models.Model):
    alert_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='alerts')
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=AlertStatus.choices, default=AlertStatus.PENDING)

    mark = models.ForeignKey('records.Mark', on_delete=models.SET_NULL, null=True, blank=True, related_name='alerts')
    attendance = models.ForeignKey('records.Attendance', on_delete=models.SET_NULL, null=True, blank=True, related_name='alerts')
    # fee = models.ForeignKey('records.Fees', on_delete=models.SET_NULL, null=True, blank=True, related_name='alerts')
    # backlog = models.ForeignKey('records.Backlogs', on_delete=models.SET_NULL, null=True, blank=True, related_name='alerts')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Alert for {self.student.user.get_full_name()} - {self.message[:40]}"
