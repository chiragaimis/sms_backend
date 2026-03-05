from rest_framework import serializers
from api.teacher.model import Teacher
from api.classmg.model import ClassRoom


class ClassRoomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'grade', 'section']


class TeacherSerializer(serializers.ModelSerializer):
    # Read-only nested list of assigned classes
    assigned_classes = ClassRoomMiniSerializer(many=True, read_only=True)

    # Write-only field to assign class IDs
    assigned_classes_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=ClassRoom.objects.all(),
        source='assigned_classes'
    )

    class Meta:
        model = Teacher
        fields = [
            'id',
            'first_name', 'last_name', 'email', 'phone',
            'subject', 'qualification', 'experience', 'join_date',
            'assigned_classes', 'assigned_classes_ids'
        ]

    # ✅ FIX: custom create to handle many-to-many relation
    def create(self, validated_data):
        assigned_classes = validated_data.pop('assigned_classes', [])
        teacher = Teacher.objects.create(**validated_data)
        for cls in assigned_classes:
            cls.teacher = teacher
            cls.save()
        return teacher

    # ✅ FIX: custom update for edit support
    def update(self, instance, validated_data):
        assigned_classes = validated_data.pop('assigned_classes', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update assigned classes mapping
        for cls in assigned_classes:
            cls.teacher = instance
            cls.save()

        return instance
