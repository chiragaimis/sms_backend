from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .model import ClassRoom
from .serializer import ClassRoomSerializer

class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [AllowAny]
