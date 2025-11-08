from django.db import models

class ExamType(models.TextChoices):
    INTERNAL = 'Internal', 'Internal'
    EXTERNAL = 'External', 'External'
    FINAL = 'Final', 'Final'

class AttendanceStatus(models.TextChoices):
    PRESENT = 'Present', 'Present'
    ABSENT = 'Absent', 'Absent'

class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey('academics.Subjects', on_delete=models.CASCADE, related_name='marks')
    exam_type = models.CharField(max_length=20, choices=ExamType.choices)
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_marks')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'marks'
        verbose_name = "Mark"   
        verbose_name_plural = "Marks"  
        ordering = ['-created_at']
        unique_together = [['student', 'subject', 'exam_type']] 

    def __str__(self):
        return f"{self.student.user.username} - {self.subject.subject_name} ({self.exam_type}): {self.grade}"


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=AttendanceStatus.choices)
    class_sub = models.ForeignKey('academics.Class_sub', on_delete=models.CASCADE, related_name='attendance_records')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_attendance')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'attendance_records'
        verbose_name = "Attendance Record"   
        verbose_name_plural = "Attendance Records"
        ordering = ['-date']
        unique_together = [['student', 'date', 'class_sub']]

    def __str__(self):
        return f"{self.student.user.username} - {self.date} - {self.status}"
    


# class FeeStatus(models.TextChoices):
#     PAID = 'Paid', 'Paid'
#     PENDING = 'Pending', 'Pending'
#     OVERDUE = 'Overdue', 'Overdue'

# class BacklogStatus(models.TextChoices):
#     PENDING = 'Pending', 'Pending'
#     CLEARED = 'Cleared', 'Cleared'

# class Fees(models.Model):
#     fee_id = models.AutoField(primary_key=True)
#     student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='fees')
#     amount_due = models.DecimalField(max_digits=10, decimal_places=2)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     due_date = models.DateField()
#     payment_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=10, choices=FeeStatus.choices)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     modified_by = models.TextField()
#     is_active = models.BooleanField(default=True)

# class Backlogs(models.Model):
#     backlog_id = models.AutoField(primary_key=True)
#     student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='backlogs')
#     subject = models.ForeignKey('academics.Subjects', on_delete=models.CASCADE, related_name='backlogs')
#     exam_type = models.CharField(max_length=20, choices=ExamType.choices)
#     status = models.CharField(max_length=10, choices=BacklogStatus.choices)
#     attempt_number = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     modified_by = models.TextField()
#     is_active = models.BooleanField(default=True)
