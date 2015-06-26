from django.db import models

# Create your models here.

class People(models.Model):
    SEX = (
        (1, 'Male'),
        (2, 'Female'),
        )

    RELATIONSHIP = (
        (18, 'Self'),
        (19, 'Self'),
        (20, 'Spouse'),
        (21, 'Unmarried Partner'),
        (22, 'Own household child'),
        (23, 'Grandchild'),
        (24, 'Parent'),
        (25, 'Brother/sister'),
        (26, 'Other relative'),
        (27, 'Foster child'),
        (28, 'Housemate/roommate'),
        (29, 'Roomer/boarder'),
        (30, 'Other non relative'),
        (40, 'Own non household child under 18'),
         )
        
    household = models.ForeignKey(HouseholdList) # TUCASEID
    respondent_identifier = models.CharField(max_length = 2) # 1 for interviewee, TULINENO
    age = models.IntegerField(default = 1) # person age TEAGE
    sex = models.IntegerField(choices = SEX) # 1 Male, 2 Female TESEX
    relationship_to_respondent = models.IntegerField(choices = RELATIONSHIP) # 18 - 40 TERRP    

#not needed, class People has this included
# class Relationship(models.Model):
#     code = models.IntegerField()
#     descriptive_name = models.CharField(max_length = 255)


class HouseholdList(models.Model):
    household_number = models.CharField(max_length = 255, primary_key=True) # tucaseid


class Respondents(models.Model):
    YES_NO = (
        (1, 'Yes'),
        (2, 'No'),
        (0, 'No - 0'),        
    )

    WEEKDAYS = (
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
        (5, 'Thursday'),
        (6, 'Friday'),
        (7, 'Saturday')
        )
        
    EMPLOYMENT_TYPE = (
        (1, 'Full Time'),
        (2, 'Part Time'),
        (3, 'Varies'),
        )

    SCHOOL_LEVEL = (
        (1, 'High School'),
        (2, 'College/University'),      
        )

    PARTNER_PRESENT_TYPE = (
        (1, 'Spouse Present'),
        (2, 'Unmarried Partner Present'),
        (3, 'No Spouse or Unmarried Partner'),
        )

    LABOR_FORCE_STATUS = (
        (1, 'Employed - at Work'),
        (2, 'Employed - Absent'),
        (3, 'Unemployed - On Layoff'),
        (4, 'Unemployed - Looking'),
        (5, 'Not in labor force'),
        )
        
    household = models.ForeignKey(HouseholdList) #TUCASEID
    statistical_weight = models.CharField(max_length = 255) # TUFINLWGT
    children_present = models.IntegerField(choices = YES_NO) # 1 yes, 2 no TRYHHCHILD
    multiple_jobs = models.IntegerField(choices = YES_NO) # 1 yes,2 no TEMJOT
    employment_type = models.IntegerField(choices = EMPLOYMENT_TYPE) # 1F, 2P TRDPFTPT,
    school_level = models.IntegerField(choices = SCHOOL_LEVEL) #1 high school 2 college,TESCHLVL
    partner_present = models.IntegerField(choices = PARTNER_PRESENT_TYPE) #1 spouse, 2Unmarried partner # None of these TRSPPRES
    partner_employed = models.IntegerField(choices = YES_NO) # 1 emp, 2 not TESPEMPNOT, Is the partner employed?
    main_job_weekly_earning = models.IntegerField() # In Cents TRERNWA,
    number_of_children = models.IntegerField() # TRCHILDNUM children under 18
    partner_employment_status = models.IntegerField(choices = EMPLOYMENT_TYPE)# 1 Ft, 2Pt, 3Varies, TRSPFTPT,
    work_week_hours = models.IntegerField() # -4 hours vary TEHRUSLT,
    inteview_day = models.IntegerField(choices = WEEKDAYS) # 1-7, sunday-saturday TUDIARYDAY,
    interview_day_holiday = models.IntegerField(choices = YES_NO) # 0 not, 1 yes TRHOLIDAY,
    time_for_eldercare = models.IntegerField() # TRTEC,
    child_care_time = models.IntegerField() # time to provide child Care TRTHH
    enrolled_in_school = models.IntegerField(choices = YES_NO) # 1Y, 2N TESCHENR
    labor_force_status = models.IntegerField(choices = LABOR_FORCE_STATUS) # 1 - 5 TELFS

    
class Activity(models.Model):
    household = models.ForeignKey(Respondents) # TUCASEID
    activity = models.ForeignKey(ActivityList) # tXXXXXX
    time = models.IntegerField() # derived

    
class ActivityList(models.Model):
    activity_code = models.CharField(max_length = 255) # tXXXXXXXX
    descriptive_name = models.CharField(max_length = 255) 

#not needed, included in class People
# class Sex(models.Model):
#     name = models.CharField(max_length = 10) # 1, 2 TESEX


