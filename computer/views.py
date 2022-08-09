from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Computer
from .serializers import ComputerSerializer

class ComputerViewSet(ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


