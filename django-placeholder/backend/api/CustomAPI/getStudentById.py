# api/student/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.Student.model import Student
from rest_framework.permissions import AllowAny

class GetStudentByIdAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id):
        try:
            # Student get by pk (id)
            student = Student.objects.get(id=student_id)
            data = {
                "id": student.id,
                "student_id": student.student_id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "phone": student.phone,
                "date_of_birth": student.date_of_birth,
                "gender": student.gender,
                "blood_group": student.blood_group,
                "address": student.address,
                "city": student.city,
                "state": student.state,
                "zip_code": student.zip_code,
                "photo": student.photo,
                "student_class": student.student_class,
                "section": student.section,
                "roll_number": student.roll_number,
                "admission_date": student.admission_date,
                "parent_name": student.parent_name,
                "parent_email": student.parent_email,
                "parent_phone": student.parent_phone,
                "parent_relation": student.parent_relation,
                "emergency_contact": student.emergency_contact,
                "medical_info": student.medical_info,
                "created_at": student.created_at,
            }
            return Response(data, status=status.HTTP_200_OK)

        except Student.DoesNotExist:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
