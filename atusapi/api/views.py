from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from respondents.models import People, Respondents, HouseholdList, Activity
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User
from .serializers import PeopleSerializer, RespondentsSerializer, HouseholdListSerializer, RespondentsDetailSerializer,\
    RespondentsActivitySerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset= People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RespondentsHouseholdMembers(generics.ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        try:
            respondent = Respondents.objects.get(id = self.kwargs['pk'])
            return People.objects.filter(household_id = respondent.household.household_id.household_number)
        except:
            return "Object not found"

class PeopleDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PeopleSerializer
    queryset = People.objects.all()


class RespondentsViewSet(viewsets.ModelViewSet):
    queryset= Respondents.objects.all()
    serializer_class = RespondentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RespondentsActivityView(generics.ListAPIView):

    serializer_class = RespondentsActivitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        try:
            respondent = Respondents.objects.get(id = self.kwargs['pk'])
            return Activity.objects.filter(household_id = respondent)#respondent.household.household_id.household_number)
        except:
            return "Object not found"

class HouseholdListView(generics.ListCreateAPIView):
    queryset = HouseholdList.objects.all()
    serializer_class = HouseholdListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HouseholdListDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = HouseholdListSerializer
    queryset = HouseholdList.objects.all()

