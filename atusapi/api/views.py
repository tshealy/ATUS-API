from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from .serializers import PeopleSerializer, RespondentsSerializer, ActivitySerializer
from respondents.models import Respondents
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User


class RespondentsViewSet(viewsets.ModelViewSet):
    queryset= Respondents.objects.all()
    serializer_class = RespondentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = BookmarkFilter
