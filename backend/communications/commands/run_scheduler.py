# communications/management/commands/run_scheduler.py
from django.core.management.base import BaseCommand
from communications.scheduler import send_nightly_alerts

class Command(BaseCommand):
    help = "Manually trigger attendance alert emails."

    def handle(self, *args, **kwargs):
        send_nightly_alerts()
        self.stdout.write(self.style.SUCCESS("Attendance alerts processed successfully!"))
