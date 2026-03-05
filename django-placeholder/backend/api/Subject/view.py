from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .model import Subject
from .serializer import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('-created_at')
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]
