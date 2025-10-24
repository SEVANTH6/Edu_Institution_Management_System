from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    ) 

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, help_text="Type of user", blank=False, null=False)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']

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

    # audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_faculties')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'faculties'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ['user__first_name', 'user__last_name']
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.designation}"





GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='student_profile'
    )
    enrollment_number = models.CharField(max_length=20, unique=True)  # usn or unique roll no.
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default='')
    address = models.TextField()
    # Academic details
    branch = models.ForeignKey('academics.Branches', on_delete=models.SET_NULL, null=True, related_name='students')
    batch = models.ForeignKey('academics.Batches', on_delete=models.SET_NULL, null=True, related_name='students')
    # Parental details
    father_name = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=15)

    mother_name = models.CharField(max_length=100)
    mother_phone = models.CharField(max_length=15)
    
    parent_email = models.EmailField()   
    
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_phone = models.CharField(max_length=15, blank=True)

    # audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_students')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['enrollment_number']

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.enrollment_number})"

