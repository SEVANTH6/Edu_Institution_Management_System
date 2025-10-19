from django.db import models

class Faculties(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True)
    department = models.ForeignKey('academics.Branches', on_delete=models.SET_NULL, null=True, related_name='faculties')
    designation = models.TextField()
    date_of_joining = models.DateField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Students(models.Model):
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
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

