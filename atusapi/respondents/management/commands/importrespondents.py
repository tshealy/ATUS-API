from django.core.management.base import BaseCommand, CommandError
from respondents.models import Respondents, People, HouseholdList, Activity, ActivityList

# Scraping tools
import random
from django.contrib.auth.models import User
import csv
import os
import sys

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('query', nargs='+', type=str)
        parser.add_argument('--respondents',
                            dest = 'respondents')
        
    def handle(self, *args, **options):
        rosterfile = options['query'][0]
        respondentsfile = options['respondents']
        #print(respondentsfile)
        delimiter = ['\t', ',', '|']
        roster_data = self.readfile(rosterfile, ',')
        respondents = self.readfile(respondentsfile, ',')
        self.import_people(roster_data)        
        self.import_respondents(respondents)
        
    def readfile(self, filename, delim, encode='utf-8'):
        data = []
        with open(filename, encoding=encode) as datafile:
            filedata = csv.reader(datafile, delimiter=delim)
            for line in filedata:
                data.append(line)
        return data

    def import_people(self, data, counts = 1000):
        '''Imports people from the roster file'''
        # remove first header row
        data = data[1:]
        counter = 0
        for line in data:
            person = People()
            person.household_id = self.household_exists(line[0])
            person.respondent_identifier = line[1]
            person.age = line[2]
            person.sex = line[4]
            person.relationship_to_respondent = line[3]
            person.save()
            counter += 1
            if counter == counts:
                break
                
    def household_exists(self, householdid):
        try:
            household_object = HouseholdList.objects.get(household_number = householdid)
            return household_object
        except:
            print("We did not find, so we are creating one")
            household_object = HouseholdList()
            household_object.household_number = householdid
            household_object.save()
            return HouseholdList(household_number = householdid)
            #return household_object

    def respondent_exists(self, respondentid):
        try:
            respondent_object = People.objects.get(household_id = respondentid, respondent_identifier = 1)
            return respondent_object
        except:
            print("We did not find, so we are creating one")
            respondent_object = People()
            respondent_object.household_id = HouseholdList(household_number = respondentid)
            respondent_object.save()
            return People(household_id = respondentid)
            #return household_object
        
    def import_respondents(self, data):
        activity_headers = data[0][24:]
        person_headers = data[0][0:24]
        print("Personal headers: {}".format(len(person_headers)))
        data = data[1:]
        counter = 0
        for line in data:                              
            personal_data = line[0:24]
            activity_data = line[24:]
            RespondentObject = Respondents()
            RespondentObject.household = self.respondent_exists(personal_data[0])
            RespondentObject.statistical_weight = personal_data[1]
            RespondentObject.children_present = personal_data[2]
            RespondentObject.labor_force_status = personal_data[9]
            RespondentObject.multiple_jobs = personal_data[10]
            RespondentObject.employment_type = personal_data[11]
            RespondentObject.enrolled_in_school = personal_data[12]
            RespondentObject.school_level = personal_data[13]
            RespondentObject.partner_present = personal_data[14]
            RespondentObject.partner_employed = personal_data[15]
            RespondentObject.main_job_weekly_earning = personal_data[16]
            RespondentObject.number_of_children = personal_data[17]
            RespondentObject.partner_employment_status = personal_data[18]
            RespondentObject.work_week_hours = personal_data[19]
            RespondentObject.interview_day = personal_data[20]
            RespondentObject.interview_day_holiday = personal_data[21]
            RespondentObject.time_for_eldercare = personal_data[22]
            RespondentObject.child_care_time = personal_data[23]   
            RespondentObject.save()
            respondent_object = Respondents.objects.get(household = self.respondent_exists(personal_data[0]))
            self.import_activity_time(respondent_object, activity_headers, activity_data)
            counter += 1
            if counter == 500:
                break

                
    def import_activity_time(self, respondent, activity_list, data):
        print("Primary key {}".format(respondent.id))
        for idx, activityid in enumerate(activity_list):
            
            if int(data[idx]) > 0:
                activity = Activity()
                print("respondent id equals = {}".format(respondent))
                activity.household_id = Respondents.objects.get(pk = respondent.id)
                activity.activity = self.activity_exists(activityid)
                activity.time = int(data[idx])
                activity.save()
            else:
                continue
            
    def activity_exists(self, activityid):
        try:
            activityObject =  ActivityList.objects.get(activity_code = activityid)
            return activityObject
        except:
            print("We are creating activity")
            activity = ActivityList()
            activity.activity_code = activityid
            activity.save()
            return activity
