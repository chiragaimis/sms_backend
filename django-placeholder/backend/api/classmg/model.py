from django.db import models
import uuid
from api.teacher.model import Teacher


class ClassRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    grade = models.CharField(max_length=10,null=True, blank=True)
    section = models.CharField(max_length=5,null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name="classes")


    def save(self, *args, **kwargs):
        self.name = f"Class {self.grade}-{self.section}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
