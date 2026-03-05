from django.db import models
from api.Student.model import Student
import uuid
from datetime import datetime
from django.utils.crypto import get_random_string

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank', 'Bank Transfer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_payments_FK')
    fee_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=50, blank=True, unique=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    bank_reference = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            # Current Academic Year format: YYYY-YYYY
            now = datetime.now()
            if now.month >= 6:  # assuming academic year starts in June
                start_year = now.year
                end_year = now.year + 1
            else:
                start_year = now.year - 1
                end_year = now.year

            academic_year = f"{start_year}-{end_year}"
            
            # Generate unique 6-digit number
            unique_number = get_random_string(length=6, allowed_chars='0123456789')

            # Combine to form receipt number
            self.receipt_number = f"SHARDA/{academic_year}/{unique_number}"

            # Ensure uniqueness
            while Payment.objects.filter(receipt_number=self.receipt_number).exists():
                unique_number = get_random_string(length=6, allowed_chars='0123456789')
                self.receipt_number = f"SHARDA/{academic_year}/{unique_number}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.fee_type} - {self.amount}"