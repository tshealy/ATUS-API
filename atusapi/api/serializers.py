__author__ = 'trippshealy'
from rest_framework import serializers
from respondents.models import HouseholdList, People, Respondents, Activity, ActivityList
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.fields import SerializerMethodField

class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = People


class RespondentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Respondents
        exclude = ('household',)


class RespondentsDetailSerializer(serializers.HyperlinkedModelSerializer):
    activities = serializers.HyperlinkedRelatedField(view_name='respondents-detail', many=True, read_only=True)
    # household_members = PeopleSerializer(many=True, read_only=True)
    _links = SerializerMethodField()

    def get__links(self, obj):
        links = {
            "household_members": reverse('householdlist-detail', kwargs=dict(pk=obj.household),
                              request=self.context.get('request'))}
        return links

    class Meta:
        model = Respondents
        fields = ('activities', '_links')

#
# class HouseholdMembersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=People

class HouseholdListSerializer(serializers.HyperlinkedModelSerializer):
    household_members = serializers.HyperlinkedRelatedField(view_name='people-detail', many=True, read_only=True)
    class Meta:
        model = HouseholdList
        fields = ("url", "household_members")
