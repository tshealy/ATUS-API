from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from respondents.models import People, Respondents, HouseholdList, Activity, ActivityList
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User
from .serializers import ActivitySerializer, ActivityListSerializer, ActivityDataSerializer
from django.db.models import Count, Avg

    
class ActivityListDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ActivityListSerializer
    queryset = ActivityList.objects.all()


class ActivityViewSet(viewsets.ModelViewSet):
    queryset= ActivityList.objects.all()
    serializer_class = ActivityListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ActivityDataView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ActivityDataSerializer
    queryset = Activity.objects.all()


