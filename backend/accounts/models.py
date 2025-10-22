from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    ) 

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, help_text="Type of user")
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_user_type_display()})"



class Faculty(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='faculty_profile'
    )
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey('academics.Branches', on_delete=models.SET_NULL, null=True, related_name='faculties')
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_faculties')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'faculties'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ['employee_id']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.designation}"


class Students(models.Model):
    # One-to-one relationship with User model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='student_profile'
    )

    # Additional student-specific fields
    student_id = models.AutoField(primary_key=True)  # usn or unique roll no.
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    branch = models.ForeignKey('academics.Branches', on_delete=models.SET_NULL, null=True, related_name='students')
    batch = models.ForeignKey('academics.Batches', on_delete=models.SET_NULL, null=True, related_name='students')
    father_name = models.TextField()
    father_phno = models.TextField()
    parents_gaurdian_mail = models.TextField()
    mother_name = models.TextField()
    mother_phno = models.TextField()
    guardian_name = models.TextField(blank=True, null=True)
    guardian_phno = models.TextField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='modified_faculties'
)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

