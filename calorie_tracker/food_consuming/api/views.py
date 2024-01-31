from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from food_consuming.api.serializers import (
    UserSerializer, FoodSerializer, ConsumeSerializer
)
from food_consuming.models import Food, Consume


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsumeViewSet(viewsets.ModelViewSet):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [permissions.IsAuthenticated]
