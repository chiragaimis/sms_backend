from rest_framework import serializers
from api.classmg.model import ClassRoom
from api.teacher.model import Teacher

class TeacherMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']

class ClassRoomSerializer(serializers.ModelSerializer):
    teacher = TeacherMiniSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Teacher.objects.all(),
        source='teacher'
    )

    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'grade', 'section', 'teacher', 'teacher_id']
