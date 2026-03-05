from rest_framework import viewsets
from .model import Teacher
from .serializer import TeacherSerializer
from rest_framework.permissions import AllowAny

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-created_at')
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
