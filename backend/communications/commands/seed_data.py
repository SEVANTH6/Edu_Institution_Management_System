from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date

from accounts.models import User, Student, Faculty
from academics.models import Branches, Batches, Classes, Subjects, Class_sub
from records.models import Attendance


class Command(BaseCommand):
    help = "Seed sample data: creates a branch, class, student, and marks one student absent."

    def handle(self, *args, **options):
        # 1️⃣ Branch
        branch, _ = Branches.objects.get_or_create(branch_name="Computer Science", defaults={"modified_by": "system"})

        # 2️⃣ Batch
        batch, _ = Batches.objects.get_or_create(
            batch_name="2025 Batch", start_year=2022, end_year=2026, defaults={"modified_by": "system"}
        )

        # 3️⃣ Faculty (class teacher)
        faculty_user, _ = User.objects.get_or_create(
            username="teacher1",
            defaults={
                "email": "teacher1@example.com",
                "user_type": "faculty",
                "first_name": "Demo",
                "last_name": "Teacher",
                "password": "teacher@123",
            },
        )
        faculty, _ = Faculty.objects.get_or_create(
            user=faculty_user,
            defaults={
                "employee_id": "FAC001",
                "department": branch,
                "designation": "Lecturer",
                "date_of_joining": date(2020, 1, 1),
                "address": "Mangalore",
            },
        )

        # 4️⃣ Class
        class_obj, _ = Classes.objects.get_or_create(
            class_name="CS-A",
            defaults={
                "class_teacher": faculty,
                "batch": batch,
                "modified_by": "system",
            },
        )

        # 5️⃣ Subject
        subject, _ = Subjects.objects.get_or_create(
            subject_name="Python Programming",
            branch=branch,
            defaults={"modified_by": "system"},
        )

        # 6️⃣ Class-Subject mapping
        class_sub, _ = Class_sub.objects.get_or_create(
            subject=subject,
            class_id=class_obj,
            faculty=faculty,
            defaults={"modified_by": "system"},
        )

        # 7️⃣ Student
        student_user, _ = User.objects.get_or_create(
            username="student1",
            defaults={
                "email": "student1@example.com",
                "user_type": "student",
                "first_name": "Test",
                "last_name": "Student",
                "password": "student@123",
            },
        )

        student, _ = Student.objects.get_or_create(
            user=student_user,
            defaults={
                "enrollment_number": "STU001",
                "date_of_birth": date(2005, 1, 1),
                "gender": "M",
                "address": "Bangalore",
                "branch": branch,
                "batch": batch,
                "father_name": "John Doe",
                "father_phone": "9876543210",
                "mother_name": "Jane Doe",
                "mother_phone": "9876543211",
                "parent_email": "www.puneethkumar1405@gmail.com",  # 👈 your email
            },
        )

        # 8️⃣ Mark Attendance (Absent)
        attendance, created = Attendance.objects.get_or_create(
            student=student,
            date=date.today(),
            class_sub=class_sub,
            defaults={"status": "Absent"},
        )

        if created:
            self.stdout.write(self.style.SUCCESS("✅ Marked student absent and email will be sent"))
        else:
            self.stdout.write(self.style.WARNING("ℹ️ Attendance already exists — no new email triggered"))

        self.stdout.write(self.style.SUCCESS("🎉 Seed data setup complete!"))
