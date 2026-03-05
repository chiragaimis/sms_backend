# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.teacher.model import Teacher
from rest_framework.permissions import AllowAny

class GetTeacherByIdAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)

            # Get assigned classes
            classes = teacher.classes.all() 
            class_list = [
                {
                    "id": str(cls.id),
                    "name": cls.name,
                    "grade": cls.grade,
                    "section": cls.section
                } for cls in classes
            ]

            # Prepare response
            data = {
                "id": str(teacher.id),
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
                "email": teacher.email,
                "phone": teacher.phone,
                "subject": teacher.subject,
                "qualification": teacher.qualification,
                "experience": teacher.experience,
                "join_date": teacher.join_date,
                "created_at": teacher.created_at,
                "updated_at": teacher.updated_at,
                "deleted_at": teacher.deleted_at,
                "classes_assigned": class_list,  
            }
            return Response(data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
