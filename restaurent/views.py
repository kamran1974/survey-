from rest_framework import viewsets
from .serializers import OpinionSerializer, ClientSerializer
from .models import Opinion, Client


class OpinionViewSet(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

