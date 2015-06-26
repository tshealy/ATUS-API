__author__ = 'trippshealy'
from rest_framework import serializers
from respondents.models import People, HouseholdList, Respondents, Activity, ActivityList
from django.contrib.auth.models import User

class PeopleSerializer(serializers.HyperlinkedIdentityField):

    class Meta:
        model = People


class RespondentsSerializer(serializers.HyperlinkedIdentityField):

    class Meta:
        model = Respondents


class ActivitySerializer(serializers.HyperlinkedIdentityField):

    class Meta:
        model = Activity