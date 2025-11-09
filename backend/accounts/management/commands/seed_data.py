"""
Management command to seed dummy data for testing
Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import datetime, timedelta
import random

from accounts.models import User, Faculty, Student
from academics.models import Branches, Batches, Subjects, Classes, Class_sub
from records.models import Mark, Attendance, ExamType, AttendanceStatus


class Command(BaseCommand):
    help = 'Seeds the database with dummy data for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            self.clear_data()

        self.stdout.write(self.style.SUCCESS('Starting data seeding...'))
        
        with transaction.atomic():
            # Create admin user first
            admin = self.create_admin()
            
            # Create academic structure
            branches = self.create_branches(admin)
            batches = self.create_batches(admin)
            subjects = self.create_subjects(branches, admin)
            
            # Create users
            faculties = self.create_faculties(branches, admin)
            students = self.create_students(branches, batches, admin)
            
            # Create classes
            classes = self.create_classes(batches, faculties, students, admin)
            class_subs = self.create_class_subjects(classes, subjects, faculties, admin)
            
            # Create records
            self.create_marks(students, subjects, admin)
            self.create_attendance(students, class_subs, admin)

        self.stdout.write(self.style.SUCCESS('✓ Data seeding completed successfully!'))
        self.print_summary()

    def clear_data(self):
        """Clear existing data"""
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
        self.stdout.write(self.style.WARNING('✓ Existing data cleared'))

    def create_admin(self):
        """Create or get admin user"""
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@institution.edu',
                'first_name': 'System',
                'last_name': 'Admin',
                'user_type': 'admin',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS('✓ Admin user created (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.SUCCESS('✓ Admin user already exists'))
        return admin

    def create_branches(self, admin):
        """Create academic branches/departments"""
        branch_names = [
            'Computer Science and Engineering',
            'Electronics and Communication Engineering',
            'Mechanical Engineering',
            'Civil Engineering',
            'Information Technology',
        ]
        
        branches = []
        for name in branch_names:
            branch, created = Branches.objects.get_or_create(
                branch_name=name,
                defaults={
                    'modified_by': str(admin.id),
                    'is_active': True,
                }
            )
            branches.append(branch)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(branches)} branches'))
        return branches

    def create_batches(self, admin):
        """Create academic batches"""
        batches_data = [
            ('Batch 2021-2025', 2021, 2025),
            ('Batch 2022-2026', 2022, 2026),
            ('Batch 2023-2027', 2023, 2027),
            ('Batch 2024-2028', 2024, 2028),
        ]
        
        batches = []
        for name, start, end in batches_data:
            batch, created = Batches.objects.get_or_create(
                batch_name=name,
                defaults={
                    'start_year': start,
                    'end_year': end,
                    'modified_by': str(admin.id),
                    'is_active': True,
                }
            )
            batches.append(batch)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(batches)} batches'))
        return batches

    def create_subjects(self, branches, admin):
        """Create subjects for each branch"""
        subjects_by_branch = {
            'Computer Science and Engineering': [
                'Data Structures', 'Algorithms', 'Database Management Systems',
                'Operating Systems', 'Computer Networks', 'Software Engineering',
                'Machine Learning', 'Artificial Intelligence'
            ],
            'Electronics and Communication Engineering': [
                'Digital Electronics', 'Analog Circuits', 'Microprocessors',
                'Signal Processing', 'Communication Systems', 'VLSI Design'
            ],
            'Mechanical Engineering': [
                'Thermodynamics', 'Fluid Mechanics', 'Machine Design',
                'Manufacturing Processes', 'CAD/CAM', 'Heat Transfer'
            ],
            'Civil Engineering': [
                'Structural Analysis', 'Concrete Technology', 'Geotechnical Engineering',
                'Transportation Engineering', 'Surveying', 'Hydraulics'
            ],
            'Information Technology': [
                'Web Technologies', 'Cloud Computing', 'Cyber Security',
                'Mobile Application Development', 'IoT', 'Big Data Analytics'
            ],
        }
        
        subjects = []
        for branch in branches:
            subject_names = subjects_by_branch.get(branch.branch_name, [])
            for subject_name in subject_names:
                subject, created = Subjects.objects.get_or_create(
                    subject_name=subject_name,
                    branch=branch,
                    defaults={
                        'modified_by': str(admin.id),
                        'is_active': True,
                    }
                )
                subjects.append(subject)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(subjects)} subjects'))
        return subjects

    def create_faculties(self, branches, admin):
        """Create faculty members"""
        faculty_data = [
            ('john.doe', 'John', 'Doe', 'john.doe@institution.edu', '+1234567890', 'FAC001', 'Professor'),
            ('jane.smith', 'Jane', 'Smith', 'jane.smith@institution.edu', '+1234567891', 'FAC002', 'Associate Professor'),
            ('robert.johnson', 'Robert', 'Johnson', 'robert.johnson@institution.edu', '+1234567892', 'FAC003', 'Professor'),
            ('sarah.williams', 'Sarah', 'Williams', 'sarah.williams@institution.edu', '+1234567893', 'FAC004', 'Assistant Professor'),
            ('michael.brown', 'Michael', 'Brown', 'michael.brown@institution.edu', '+1234567894', 'FAC005', 'Lecturer'),
            ('emily.davis', 'Emily', 'Davis', 'emily.davis@institution.edu', '+1234567895', 'FAC006', 'Associate Professor'),
            ('david.miller', 'David', 'Miller', 'david.miller@institution.edu', '+1234567896', 'FAC007', 'Professor'),
            ('lisa.wilson', 'Lisa', 'Wilson', 'lisa.wilson@institution.edu', '+1234567897', 'FAC008', 'Assistant Professor'),
            ('james.moore', 'James', 'Moore', 'james.moore@institution.edu', '+1234567898', 'FAC009', 'Lecturer'),
            ('patricia.taylor', 'Patricia', 'Taylor', 'patricia.taylor@institution.edu', '+1234567899', 'FAC010', 'Associate Professor'),
        ]
        
        faculties = []
        for idx, (username, first_name, last_name, email, phone, emp_id, designation) in enumerate(faculty_data):
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'user_type': 'faculty',
                    'phone_number': phone,
                }
            )
            if created:
                user.set_password('faculty123')
                user.save()
            
            faculty, created = Faculty.objects.get_or_create(
                user=user,
                defaults={
                    'employee_id': emp_id,
                    'department': branches[idx % len(branches)],
                    'designation': designation,
                    'date_of_joining': datetime(2020 + (idx % 5), 1 + (idx % 12), 1).date(),
                    'address': f'{100 + idx} Faculty Lane, University City, State {10000 + idx}',
                    'modified_by': admin,
                    'is_active': True,
                }
            )
            faculties.append(faculty)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(faculties)} faculty members'))
        return faculties

    def create_students(self, branches, batches, admin):
        """Create student records"""
        first_names = ['Alex', 'Sam', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Avery', 'Quinn', 'Reese',
                      'Cameron', 'Drew', 'Skylar', 'Parker', 'Rowan', 'Blake', 'Hayden', 'Dakota', 'Sage', 'River']
        last_names = ['Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
                     'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright']
        
        students = []
        student_count = 0
        
        for batch in batches:
            for branch in branches:
                # Create 5-8 students per batch-branch combination
                num_students = random.randint(5, 8)
                
                for i in range(num_students):
                    student_count += 1
                    first_name = random.choice(first_names)
                    last_name = random.choice(last_names)
                    username = f'student{student_count:03d}'
                    
                    user, created = User.objects.get_or_create(
                        username=username,
                        defaults={
                            'email': f'{username}@student.institution.edu',
                            'first_name': first_name,
                            'last_name': last_name,
                            'user_type': 'student',
                            'phone_number': f'+98765{student_count:05d}',
                        }
                    )
                    if created:
                        user.set_password('student123')
                        user.save()
                    
                    enrollment_num = f'STU{batch.start_year}{branch.branch_id:02d}{i+1:03d}'
                    
                    student, created = Student.objects.get_or_create(
                        user=user,
                        defaults={
                            'enrollment_number': enrollment_num,
                            'date_of_birth': datetime(2000 + random.randint(0, 5), random.randint(1, 12), random.randint(1, 28)).date(),
                            'gender': random.choice(['M', 'F']),
                            'address': f'{student_count} Student Street, City, State {20000 + student_count}',
                            'branch': branch,
                            'batch': batch,
                            'father_name': f'Father of {first_name}',
                            'father_phone': f'+91987654{student_count:04d}',
                            'mother_name': f'Mother of {first_name}',
                            'mother_phone': f'+91876543{student_count:04d}',
                            'parent_email': f'parent{student_count}@email.com',
                            'guardian_name': '',
                            'guardian_phone': '',
                            'modified_by': admin,
                            'is_active': True,
                        }
                    )
                    students.append(student)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(students)} students'))
        return students

    def create_classes(self, batches, faculties, students, admin):
        """Create classes"""
        classes = []
        
        for batch in batches:
            # Create 2-3 classes per batch
            for i in range(random.randint(2, 3)):
                class_name = f'{batch.batch_name} - Section {chr(65 + i)}'
                
                class_obj, created = Classes.objects.get_or_create(
                    class_name=class_name,
                    defaults={
                        'class_teacher': random.choice(faculties),
                        'batch': batch,
                        'modified_by': str(admin.id),
                        'is_active': True,
                    }
                )
                
                # Assign students to this class
                batch_students = [s for s in students if s.batch == batch]
                if batch_students:
                    students_for_class = random.sample(
                        batch_students, 
                        min(len(batch_students), random.randint(8, 15))
                    )
                    class_obj.students.set(students_for_class)
                
                classes.append(class_obj)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(classes)} classes'))
        return classes

    def create_class_subjects(self, classes, subjects, faculties, admin):
        """Create class-subject mappings"""
        class_subs = []
        
        for class_obj in classes:
            # Get subjects relevant to the class's students' branches
            class_students = class_obj.students.all()
            if not class_students:
                continue
                
            student_branches = set(s.branch for s in class_students if s.branch)
            relevant_subjects = [s for s in subjects if s.branch in student_branches]
            
            # Assign 4-6 subjects per class
            num_subjects = min(len(relevant_subjects), random.randint(4, 6))
            selected_subjects = random.sample(relevant_subjects, num_subjects)
            
            for subject in selected_subjects:
                # Assign faculty from the same branch if possible
                branch_faculties = [f for f in faculties if f.department == subject.branch]
                faculty = random.choice(branch_faculties) if branch_faculties else random.choice(faculties)
                
                class_sub, created = Class_sub.objects.get_or_create(
                    subject=subject,
                    class_id=class_obj,
                    defaults={
                        'faculty': faculty,
                        'modified_by': str(admin.id),
                        'is_active': True,
                    }
                )
                class_subs.append(class_sub)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(class_subs)} class-subject mappings'))
        return class_subs

    def create_marks(self, students, subjects, admin):
        """Create marks/grades for students"""
        exam_types = [ExamType.INTERNAL, ExamType.EXTERNAL, ExamType.FINAL]
        marks_created = 0
        
        for student in students:
            # Get subjects for student's branch
            student_subjects = [s for s in subjects if s.branch == student.branch]
            
            for subject in student_subjects[:6]:  # Limit to 6 subjects per student
                for exam_type in exam_types:
                    score = random.randint(40, 100)
                    grade = self.get_grade(score)
                    
                    mark, created = Mark.objects.get_or_create(
                        student=student,
                        subject=subject,
                        exam_type=exam_type,
                        defaults={
                            'score': score,
                            'grade': grade,
                            'modified_by': admin,
                            'is_active': True,
                        }
                    )
                    if created:
                        marks_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {marks_created} marks'))

    def create_attendance(self, students, class_subs, admin):
        """Create attendance records"""
        attendance_created = 0
        start_date = datetime.now().date() - timedelta(days=90)  # Last 3 months
        
        for student in students:
            # Get class_subs for this student's classes
            student_classes = student.enrolled_classes.all()
            student_class_subs = [cs for cs in class_subs if cs.class_id in student_classes]
            
            if not student_class_subs:
                continue
            
            # Create attendance for random days
            for day_offset in range(0, 90, random.randint(2, 4)):  # Not every day
                date = start_date + timedelta(days=day_offset)
                
                # Skip weekends
                if date.weekday() >= 5:
                    continue
                
                for class_sub in random.sample(student_class_subs, min(len(student_class_subs), random.randint(2, 4))):
                    # 85% present, 15% absent
                    status = random.choices(
                        [AttendanceStatus.PRESENT, AttendanceStatus.ABSENT],
                        weights=[85, 15]
                    )[0]
                    
                    attendance, created = Attendance.objects.get_or_create(
                        student=student,
                        date=date,
                        class_sub=class_sub,
                        defaults={
                            'status': status,
                            'modified_by': admin,
                            'is_active': True,
                        }
                    )
                    if created:
                        attendance_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {attendance_created} attendance records'))

    def get_grade(self, score):
        """Calculate grade based on score"""
        if score >= 90:
            return 'A+'
        elif score >= 80:
            return 'A'
        elif score >= 70:
            return 'B+'
        elif score >= 60:
            return 'B'
        elif score >= 50:
            return 'C'
        elif score >= 40:
            return 'D'
        else:
            return 'F'

    def print_summary(self):
        """Print summary of created data"""
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('DATABASE SUMMARY'))
        self.stdout.write(self.style.SUCCESS('='*60))
        
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'  - Admins: {User.objects.filter(user_type="admin").count()}')
        self.stdout.write(f'  - Faculty: {User.objects.filter(user_type="faculty").count()}')
        self.stdout.write(f'  - Students: {User.objects.filter(user_type="student").count()}')
        
        self.stdout.write(f'\nAcademics:')
        self.stdout.write(f'  - Branches: {Branches.objects.count()}')
        self.stdout.write(f'  - Batches: {Batches.objects.count()}')
        self.stdout.write(f'  - Subjects: {Subjects.objects.count()}')
        self.stdout.write(f'  - Classes: {Classes.objects.count()}')
        self.stdout.write(f'  - Class-Subjects: {Class_sub.objects.count()}')
        
        self.stdout.write(f'\nRecords:')
        self.stdout.write(f'  - Marks: {Mark.objects.count()}')
        self.stdout.write(f'  - Attendance: {Attendance.objects.count()}')
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('TEST CREDENTIALS'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(self.style.WARNING('Admin:'))
        self.stdout.write('  Username: admin')
        self.stdout.write('  Password: admin123')
        
        self.stdout.write(self.style.WARNING('\nFaculty (all):'))
        self.stdout.write('  Username: john.doe, jane.smith, etc.')
        self.stdout.write('  Password: faculty123')
        
        self.stdout.write(self.style.WARNING('\nStudents (all):'))
        self.stdout.write('  Username: student001, student002, etc.')
        self.stdout.write('  Password: student123')
        
        self.stdout.write(self.style.SUCCESS('='*60 + '\n'))
