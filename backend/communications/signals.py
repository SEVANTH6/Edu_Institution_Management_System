# communications/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from records.models import Attendance
from .models import ParentAlerts
from .utils import send_parent_email


@receiver(post_save, sender=Attendance)
def create_absent_alert(sender, instance, created, **kwargs):
    """
    Send parent alert immediately when student is marked Absent.
    """
    if instance.status == "Absent":
        if not ParentAlerts.objects.filter(attendance=instance).exists():
            alert = ParentAlerts.objects.create(
                student=instance.student,
                message=f"Your child was marked absent on {instance.date} for {instance.class_sub}.",
                attendance=instance,
                timestamp=timezone.now(),
                modified_by="system",
            )
            send_parent_email(alert)
