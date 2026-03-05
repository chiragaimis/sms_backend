from rest_framework import serializers
from .model import Payment
from api.Student.model import Student


class PaymentSerializer(serializers.ModelSerializer):
    student_details = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'
        # Add this line to include student_details in response
        extra_fields = ['student_details']

    def get_student_details(self, obj):
        student = obj.student
        return {
            "first_name": student.first_name,
            "last_name": student.last_name,
            "student_class": f"{student.student_class}-{student.section}"
        }
