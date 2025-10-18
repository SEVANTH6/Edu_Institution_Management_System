from django.db import models
from accounts.models import *
from records.models import *

# class AlertStatus(models.TextChoices):
#     SENT = 'Sent', 'Sent'
#     READ = 'Read', 'Read

# class ParentAlerts(models.Model):
#     alert_id = models.AutoField(primary_key=True)
#     student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='alerts')
#     message = models.TextField()
#     timestamp = models.DateTimeField()
#     status = models.CharField(max_length=10, choices=AlertStatus.choices)

#     # Links to most relevant context
#     fee = models.ForeignKey(Fees, on_delete=models.SET_NULL, null=True, related_name='alerts')
#     mark = models.ForeignKey(Marks, on_delete=models.SET_NULL, null=True, related_name='alerts')
#     attendance = models.ForeignKey(Attendance, on_delete=models.SET_NULL, null=True, related_name='alerts')
#     backlog = models.ForeignKey(Backlogs, on_delete=models.SET_NULL, null=True, related_name='alerts')

#     created_at = models.DateTimeField()
#     modified_at = models.DateTimeField()
#     modified_by = models.TextField()
#     is_active = models.BooleanField(default=True)
