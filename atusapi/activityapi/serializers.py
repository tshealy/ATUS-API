from rest_framework import serializers
from respondents.models import HouseholdList, People, Respondents, Activity, ActivityList
from django.contrib.auth.models import User


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Activity


class ActivityListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ActivityList
        fields = ('id', 'url', 'activity_code', 'descriptive_name')
