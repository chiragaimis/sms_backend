import uuid
from django.db import models
from api.teacher.model import Teacher  

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,null=True, blank=True)
    code = models.CharField(max_length=20, unique=True,null=True, blank=True)
    grade = models.CharField(max_length=20,null=True, blank=True)
    type = models.CharField(max_length=20, choices=[("Core", "Core"), ("Elective", "Elective")])
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name="subjects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
