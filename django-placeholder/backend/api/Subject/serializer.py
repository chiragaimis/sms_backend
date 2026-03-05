from rest_framework import serializers
from .model import Subject
from api.teacher.serializer import TeacherSerializer  

class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'grade', 'type', 'teacher', 'teacher_name', 'created_at']

    def get_teacher_name(self, obj):
        return f"{obj.teacher.first_name} {obj.teacher.last_name}" if obj.teacher else None
