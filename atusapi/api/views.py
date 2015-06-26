from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from respondents.models import People, Respondents, HouseholdList, Activity #, ActivityList
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User
from .serializers import PeopleSerializer, RespondentsSerializer, ActivitySerializer, HouseholdListSerializer
# ActivityListSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset= People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RespondentsViewSet(viewsets.ModelViewSet):
    queryset= Respondents.objects.all()
    serializer_class = RespondentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = <Create Filter>


class ActivityViewSet(viewsets.ModelViewSet):
    queryset= Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#
# class ActivityListView(generics.ListCreateAPIView):
#     queryset = HouseholdList.objects.all()
#     serializer_class = ActivityListSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class ActivityListDetailView(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = ActivityListSerializer
#     queryset = ActivityList.objects.all()


class HouseholdListView(generics.ListCreateAPIView):
    queryset = HouseholdList.objects.all()
    serializer_class = HouseholdListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HouseholdListDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = HouseholdListSerializer
    queryset = HouseholdList.objects.all()

#
# {
#     "statistical_weight": "12345",
#     "children_present": 1,
#     "multiple_jobs": 1,
#     "employment_type": 1,
#     "school_level": 2,
#     "partner_present": 1,
#     "partner_employed": 1,
#     "main_job_weekly_earning": 70000,
#     "number_of_children": 1,
#     "partner_employment_status": 1,
#     "work_week_hours": 4,
#     "inteview_day": 1,
#     "interview_day_holiday": 1,
#     "time_for_eldercare": 12,
#     "child_care_time": 12,
#     "enrolled_in_school": 1,
#     "labor_force_status": 1,
#     "household": "01"
# }