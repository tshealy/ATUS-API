from rest_framework import serializers
from respondents.models import HouseholdList, People, Respondents, Activity, ActivityList
from django.contrib.auth.models import User
from django.db.models import Count, Avg


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Activity


class ActivityListSerializer(serializers.HyperlinkedModelSerializer):
    respondent_counts = serializers.IntegerField(source = 'activity_set.count', read_only=True)
    class Meta:
        model = ActivityList
        fields = ('id', 'url', 'respondent_counts', 'activity_code', 'descriptive_name')


class ActivityDataSerializer(serializers.HyperlinkedModelSerializer):
    minute_counts = serializers.IntegerField(source = 'activity_set', read_only=True)
    class Meta:
        model = ActivityList
        fields = ('minute_counts',)