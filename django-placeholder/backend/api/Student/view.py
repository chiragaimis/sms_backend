from rest_framework import viewsets
from .model import Student
from .serializer import StudentSerializer
from rest_framework.permissions import AllowAny


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]  