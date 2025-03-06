from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('proctor', 'Proctor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')
    roll_number = models.CharField(max_length=15, unique=True)  
    phone_number = models.CharField(max_length=15, blank=True, null=True)
# Proctor Model (Linked to CustomUser)
class Proctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

# Student Model (Linked to CustomUser)
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=1)
    roll_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    father_mobile = models.CharField(max_length=15, null=True, blank=True)
    mother_mobile = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    passport_photo = models.ImageField(upload_to='passport_photos/', null=True, blank=True)
    proctor = models.ForeignKey(Proctor, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

# Attendance Model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)  # True = Present, False = Absent

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.status else 'Absent'}"

# Marks Model
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    test_type = models.CharField(max_length=50, choices=[('Class Test', 'Class Test'), ('Sessional', 'Sessional')])
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.test_type} - {self.marks_obtained}/{self.total_marks}"

# Digital Signatures (For Proctor & Parent Approval)
class Signature(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    proctor_signed = models.BooleanField(default=False)
    parent_signed = models.BooleanField(default=False)

    def __str__(self):
        return f"Signatures - {self.student.name}"
