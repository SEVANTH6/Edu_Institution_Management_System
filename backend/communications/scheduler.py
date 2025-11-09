# communications/scheduler.py
from datetime import date
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler

from .models import ParentAlerts
from .utils import send_parent_email
from records.models import Attendance


def send_nightly_alerts():
    """
    Runs every midnight to send parent alerts for absences.
    """
    today = date.today()
    print(f"[scheduler] Running attendance alerts for {today}")

    absences = Attendance.objects.filter(date=today, status="Absent")

    for att in absences:
        if not ParentAlerts.objects.filter(attendance=att).exists():
            alert = ParentAlerts.objects.create(
                student=att.student,
                message=f"Your child was absent on {att.date} for {att.class_sub}.",
                attendance=att,
                timestamp=timezone.now(),
                modified_by="system",
            )
            send_parent_email(alert)
            print(f"[scheduler] Email sent for {att.student.user.get_full_name()}")

    print("[scheduler] Attendance check complete.")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_nightly_alerts, "cron", hour=0, minute=0)  # midnight
    scheduler.start()
    print("[scheduler] started (attendance-only mode)")
