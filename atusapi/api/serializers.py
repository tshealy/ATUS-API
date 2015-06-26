__author__ = 'trippshealy'
from rest_framework import serializers
from respondents.models import HouseholdList, People, Respondents, Activity, ActivityList
from django.contrib.auth.models import User

class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = People


class RespondentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Respondents


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity


class ActivityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityList


class HouseholdListSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseholdList