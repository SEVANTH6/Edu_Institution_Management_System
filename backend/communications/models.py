from django.db import models


class AlertStatus(models.TextChoices):
    SENT = 'Sent', 'Sent'
    READ = 'Read', 'Read'

class ParentAlerts(models.Model):
    alert_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='alerts')
    message = models.TextField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=10, choices=AlertStatus.choices)

    # Links to most relevant context
    # fee = models.ForeignKey('records.Fees', on_delete=models.SET_NULL, null=True, related_name='alerts')  # Commented - Fees model not active
    mark = models.ForeignKey('records.Mark', on_delete=models.SET_NULL, null=True, related_name='alerts')  # Updated: Marks → Mark
    attendance = models.ForeignKey('records.Attendance', on_delete=models.SET_NULL, null=True, related_name='alerts')
    # backlog = models.ForeignKey('records.Backlogs', on_delete=models.SET_NULL, null=True, related_name='alerts')  # Commented - Backlogs model not active
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)
