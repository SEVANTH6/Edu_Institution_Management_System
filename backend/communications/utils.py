# communications/utils.py

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from .models import ParentAlerts


def send_parent_email(alert: ParentAlerts):
    student = alert.student
    parent_email = student.parent_email
    if not parent_email:
        return

    subject = f"Update about {student.user.get_full_name()}"
    context = {
        "student": student,
        "message": alert.message,
        "timestamp": timezone.now(),
    }

    text_body = render_to_string("communication/email/parent_alert.txt", context)
    html_body = render_to_string("communication/email/parent_alert.html", context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        to=[parent_email]
    )
    email.attach_alternative(html_body, "text/html")
    email.send(fail_silently=True)

    alert.status = "Sent"  # ✅ Fixed line
    alert.save(update_fields=["status"])
