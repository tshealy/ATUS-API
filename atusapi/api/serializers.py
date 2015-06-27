__author__ = 'trippshealy'
from rest_framework import serializers
from respondents.models import HouseholdList, People, Respondents, Activity, ActivityList
from django.contrib.auth.models import User

class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = People


class RespondentsSerializer(serializers.HyperlinkedModelSerializer):
    # activity = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Respondents
        # fields = ('')


class HouseholdListSerializer(serializers.HyperlinkedModelSerializer):
    household_members = serializers.HyperlinkedRelatedField(view_name='people-detail', many=True, read_only=True)
    class Meta:
        model = HouseholdList
        fields = ("url", "household_members")
