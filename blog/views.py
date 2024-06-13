from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from blog.models import *
from blog.serializers import *


class OdamViewSet(viewsets.ModelViewSet):
    queryset = Odam.objects.all()
    serializer_class = OdamSerializer
    permission_classes = [AllowAny]


class IkonViewSet(viewsets.ModelViewSet):
    queryset = Ikon.objects.all()
    serializer_class = IkonSerializer
    permission_classes = [AllowAny]


class SumpermisionViewSet(viewsets.ModelViewSet):
    queryset = Sumpermision.objects.all()
    serializer_class = SumpermisionSerializer
    permission_classes = [AllowAny]


class SponsrViewSet(viewsets.ModelViewSet):
    queryset = Sponsr.objects.all()
    serializer_class = SponsrSerializer
    permission_classes = [AllowAny]



class MaqolaViewSet(viewsets.ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
