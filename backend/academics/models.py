from django.db import models

class Branches(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.TextField()
    HOD = models.ForeignKey('accounts.Faculty', on_delete=models.SET_NULL, null=True, related_name='headed_branches')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.branch_name
    

class Batches(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch_name = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.batch_name

class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.TextField()
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, related_name='subjects')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject_name

class Classes(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.TextField()
    class_teacher = models.ForeignKey('accounts.Faculty', on_delete=models.SET_NULL, null=True, related_name='teaching_classes')
    batch = models.ForeignKey(Batches, on_delete=models.SET_NULL, null=True, related_name='classes')
    students = models.ManyToManyField('accounts.Student', related_name='enrolled_classes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.class_name
    
class Class_sub(models.Model):
    class_sub_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='class_subjects')
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='subjects')
    faculty = models.ForeignKey('accounts.Faculty', on_delete=models.SET_NULL, null=True, related_name='subject_classes')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.class_sub_id)