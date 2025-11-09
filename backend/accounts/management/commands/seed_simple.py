from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Faculty, Student
from academics.models import Branches, Batches, Subjects, Classes, Class_sub
from records.models import Attendance, Mark
from datetime import date, timedelta

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds the database with simple dummy data (5-6 records each)'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting simple database seeding...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Attendance.objects.all().delete()
        Mark.objects.all().delete()
        Class_sub.objects.all().delete()
        Classes.objects.all().delete()
        Subjects.objects.all().delete()
        Student.objects.all().delete()
        Faculty.objects.all().delete()
        Batches.objects.all().delete()
        Branches.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        # Create Admin User
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@institution.edu',
                'first_name': 'Admin',
                'last_name': 'User',
                'user_type': 'admin'
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('✓ Created admin user'))
        else:
            self.stdout.write(self.style.WARNING('✓ Admin user already exists'))

        # Create 3 Branches
        cs_branch = Branches.objects.create(branch_name='Computer Science', modified_by='admin')
        ec_branch = Branches.objects.create(branch_name='Electronics', modified_by='admin')
        me_branch = Branches.objects.create(branch_name='Mechanical', modified_by='admin')
        self.stdout.write(self.style.SUCCESS('✓ Created 3 branches'))

        # Create 2 Batches
        batch_2023 = Batches.objects.create(batch_name='Batch 2023-2027', start_year=2023, end_year=2027, modified_by='admin')
        batch_2024 = Batches.objects.create(batch_name='Batch 2024-2028', start_year=2024, end_year=2028, modified_by='admin')
        self.stdout.write(self.style.SUCCESS('✓ Created 2 batches'))

        # Create 5 Faculty Members
        faculties = []
        faculty_data = [
            ('john.doe', 'John', 'Doe', 'FAC001', 'Professor', cs_branch),
            ('jane.smith', 'Jane', 'Smith', 'FAC002', 'Associate Professor', cs_branch),
            ('bob.wilson', 'Bob', 'Wilson', 'FAC003', 'Assistant Professor', ec_branch),
            ('alice.brown', 'Alice', 'Brown', 'FAC004', 'Lecturer', ec_branch),
            ('mike.davis', 'Mike', 'Davis', 'FAC005', 'Professor', me_branch),
        ]
        
        for username, fname, lname, emp_id, designation, branch in faculty_data:
            user = User.objects.create_user(
                username=username,
                email=f'{username}@institution.edu',
                password='faculty123',
                first_name=fname,
                last_name=lname,
                user_type='faculty',
                phone_number=f'+91900000{len(faculties)+1:04d}'
            )
            faculty = Faculty.objects.create(
                user=user,
                employee_id=emp_id,
                department=branch,
                designation=designation,
                date_of_joining='2020-07-01',
                address=f'{len(faculties)+1} Faculty Street, City',
                modified_by=admin_user
            )
            faculties.append(faculty)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(faculties)} faculty members'))

        # Create 3 Subjects per branch
        subjects = []
        subjects.append(Subjects.objects.create(subject_name='Data Structures', branch=cs_branch, modified_by='admin'))
        subjects.append(Subjects.objects.create(subject_name='Algorithms', branch=cs_branch, modified_by='admin'))
        subjects.append(Subjects.objects.create(subject_name='Digital Electronics', branch=ec_branch, modified_by='admin'))
        subjects.append(Subjects.objects.create(subject_name='Signal Processing', branch=ec_branch, modified_by='admin'))
        subjects.append(Subjects.objects.create(subject_name='Thermodynamics', branch=me_branch, modified_by='admin'))
        subjects.append(Subjects.objects.create(subject_name='Fluid Mechanics', branch=me_branch, modified_by='admin'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(subjects)} subjects'))

        # Create 6 Students
        students = []
        student_data = [
            ('aarav.sharma', 'Aarav', 'Sharma', 'STU202301001', cs_branch, batch_2023),
            ('diya.patel', 'Diya', 'Patel', 'STU202301002', cs_branch, batch_2023),
            ('vivaan.kumar', 'Vivaan', 'Kumar', 'STU202302001', ec_branch, batch_2023),
            ('ananya.singh', 'Ananya', 'Singh', 'STU202302002', ec_branch, batch_2023),
            ('arjun.reddy', 'Arjun', 'Reddy', 'STU202401001', me_branch, batch_2024),
            ('ishaan.verma', 'Ishaan', 'Verma', 'STU202401002', me_branch, batch_2024),
        ]
        
        for username, fname, lname, enrollment, branch, batch in student_data:
            user = User.objects.create_user(
                username=username,
                email=f'{username}@student.edu',
                password='student123',
                first_name=fname,
                last_name=lname,
                user_type='student',
                phone_number=f'+91800000{len(students)+1:04d}'
            )
            student = Student.objects.create(
                user=user,
                enrollment_number=enrollment,
                date_of_birth='2005-05-15',
                gender='M' if len(students) % 2 == 0 else 'F',
                address=f'{len(students)+1} Student Street, City',
                branch=branch,
                batch=batch,
                father_name=f'Father {lname}',
                father_phone=f'+91700000{len(students)+1:04d}',
                mother_name=f'Mother {lname}',
                mother_phone=f'+91600000{len(students)+1:04d}',
                parent_email=f'parent.{username}@gmail.com',
                modified_by=admin_user
            )
            students.append(student)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(students)} students'))

        # Create 2 Classes
        class1 = Classes.objects.create(
            class_name='CS-2023-Sem1',
            class_teacher=faculties[0],
            batch=batch_2023,
            modified_by='admin'
        )
        class1.students.set([s for s in students if s.branch == cs_branch])
        
        class2 = Classes.objects.create(
            class_name='EC-2023-Sem1',
            class_teacher=faculties[2],
            batch=batch_2023,
            modified_by='admin'
        )
        class2.students.set([s for s in students if s.branch == ec_branch])
        self.stdout.write(self.style.SUCCESS('✓ Created 2 classes'))

        # Create Class-Subject mappings
        cs1 = Class_sub.objects.create(subject=subjects[0], class_id=class1, faculty=faculties[0], modified_by='admin')
        cs2 = Class_sub.objects.create(subject=subjects[1], class_id=class1, faculty=faculties[1], modified_by='admin')
        cs3 = Class_sub.objects.create(subject=subjects[2], class_id=class2, faculty=faculties[2], modified_by='admin')
        self.stdout.write(self.style.SUCCESS('✓ Created 3 class-subject mappings'))

        # Create some Attendance records
        for student in students[:4]:
            for i in range(3):
                Attendance.objects.create(
                    student=student,
                    class_sub=cs1 if student.branch == cs_branch else cs3,
                    date=date.today() - timedelta(days=i),
                    status='Present',
                    modified_by=admin_user
                )
        self.stdout.write(self.style.SUCCESS('✓ Created 12 attendance records'))

        # Create some Mark records
        for student in students[:4]:
            Mark.objects.create(
                student=student,
                subject=subjects[0] if student.branch == cs_branch else subjects[2],
                exam_type='Internal',
                score=85,
                grade='A',
                modified_by=admin_user
            )
        self.stdout.write(self.style.SUCCESS('✓ Created 4 mark records'))

        self.stdout.write(self.style.SUCCESS('\n✅ Database seeding completed!'))
        self.stdout.write('\nLogin credentials:')
        self.stdout.write('  Admin:   username=admin, password=admin123')
        self.stdout.write('  Faculty: username=john.doe, password=faculty123')
        self.stdout.write('  Student: username=aarav.sharma, password=student123')
