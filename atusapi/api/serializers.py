__author__ = 'trippshealy'
from rest_framework import serializers
from respondents.models import HouseholdList, People, Respondents, Activity, ActivityList
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.fields import SerializerMethodField


class RespondentsSerializer(serializers.HyperlinkedModelSerializer):

    _links = SerializerMethodField()
    def get__links(self, obj):
        links = {
            "activities": reverse('respondent-activities', kwargs=dict(pk=obj.id),
                              request=self.context.get('request')),
            "household_members": reverse('household-members', kwargs=dict(pk=obj.id),
                              request=self.context.get('request'))
        }
        return links

    class Meta:
        model = Respondents
        fields = ('url', 'statistical_weight', 'children_present', 'labor_force_status', 'multiple_jobs',\
                  'employment_type', 'enrolled_in_school', 'school_level',  'partner_present', 'partner_employed',\
                  'main_job_weekly_earning', 'number_of_children', 'partner_employment_status', 'work_week_hours',\
                  'interview_day', 'interview_day_holiday', 'time_for_eldercare', 'child_care_time', '_links')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People


class RespondentsActivitySerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.CharField()
    class Meta:
        model = Activity
        fields = ('activity','time')

class RespondentsDetailSerializer(serializers.HyperlinkedModelSerializer):
    activities = RespondentsActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Respondents
        fields = ('activities',)


class HouseholdListSerializer(serializers.HyperlinkedModelSerializer):
    household_members = serializers.HyperlinkedRelatedField(view_name='people-detail', many=True, read_only=True)

    class Meta:
        model = HouseholdList
        fields = ("url", 'household_members')

