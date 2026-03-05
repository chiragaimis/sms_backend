from django.db import models
import random

class Student(models.Model):
    student_id = models.CharField(max_length=6,unique=True,editable=False)
    # Personal Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    photo = models.TextField(blank=True, null=True)  

    # Academic Info
    student_class = models.CharField(max_length=10)
    section = models.CharField(max_length=5)
    roll_number = models.CharField(max_length=20)
    admission_date = models.DateField()

    # Parent / Guardian Info
    parent_name = models.CharField(max_length=100)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=20)
    parent_relation = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=20)
    medical_info = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.student_id:
            while True:
                random_id = str(random.randint(100000, 999999))
                if not Student.objects.filter(student_id=random_id).exists():
                    self.student_id = random_id
                    break
        super().save(*args, **kwargs)