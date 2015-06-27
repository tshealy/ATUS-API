from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from respondents.models import People, Respondents, HouseholdList, Activity
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User
from .serializers import PeopleSerializer, RespondentsSerializer, HouseholdListSerializer, RespondentsDetailSerializer



class PeopleViewSet(viewsets.ModelViewSet):
    queryset= People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PeopleDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PeopleSerializer
    queryset = People.objects.all()


class RespondentsViewSet(viewsets.ModelViewSet):
    queryset= Respondents.objects.all()
    serializer_class = RespondentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = <Create Filter>

class RespondentsDetailView(generics.RetrieveAPIView):
    queryset= Respondents.objects.all()
    serializer_class = RespondentsDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HouseholdListView(generics.ListCreateAPIView):
    queryset = HouseholdList.objects.all()
    serializer_class = HouseholdListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HouseholdListDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = HouseholdListSerializer
    queryset = HouseholdList.objects.all()



