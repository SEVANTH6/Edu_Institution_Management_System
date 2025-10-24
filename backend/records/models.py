from django.db import models


class FeeStatus(models.TextChoices):
    PAID = 'Paid', 'Paid'
    PENDING = 'Pending', 'Pending'
    OVERDUE = 'Overdue', 'Overdue'


class ExamType(models.TextChoices):
    INTERNAL = 'Internal', 'Internal'
    EXTERNAL = 'External', 'External'
    FINAL = 'Final', 'Final'


class BacklogStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CLEARED = 'Cleared', 'Cleared'


class AttendanceStatus(models.TextChoices):
    PRESENT = 'Present', 'Present'
    ABSENT = 'Absent', 'Absent'
    LEAVE = 'Leave', 'Leave'


class Fees(models.Model):
    fee_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='fees')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=FeeStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)


class Marks(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey('academics.Subjects', on_delete=models.CASCADE, related_name='marks')
    exam_type = models.CharField(max_length=20, choices=ExamType.choices)
    score = models.IntegerField()
    grade = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)


class Backlogs(models.Model):
    backlog_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='backlogs')
    subject = models.ForeignKey('academics.Subjects', on_delete=models.CASCADE, related_name='backlogs')
    exam_type = models.CharField(max_length=20, choices=ExamType.choices)
    status = models.CharField(max_length=10, choices=BacklogStatus.choices)
    attempt_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=AttendanceStatus.choices)
    class_sub = models.ForeignKey('academics.Class_sub', on_delete=models.CASCADE, related_name='attendance_records')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)