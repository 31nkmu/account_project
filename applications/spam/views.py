from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.spam.models import Spam
from applications.spam.serializer import SpamSerializer


class SpamViewSet(ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
