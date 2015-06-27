from django.db import models

# Create your models here.

class HouseholdList(models.Model):
    household_number = models.CharField(max_length = 255, primary_key=True) # tucaseid

    def __str__(self):
        return self.household_number
    
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
        
    household_id = models.ForeignKey(HouseholdList, related_name='household_members') # TUCASEID
    respondent_identifier = models.CharField(blank=True, max_length = 2) # 1 for interviewee, TULINENO
    age = models.IntegerField(blank=True, default = 1) # person age TEAGE
    sex = models.IntegerField(blank=True, choices = SEX) # 1 Male, 2 Female TESEX
    relationship_to_respondent = models.IntegerField(blank=True, choices = RELATIONSHIP) # 18 - 40 TERRP    
    def __str__(self):
        return "{} - {}".format(self.household_id, self.respondent_identifier)
#not needed, class People has this included
# class Relationship(models.Model):
#     code = models.IntegerField()
#     descriptive_name = models.CharField(max_length = 255)


    
class ActivityList(models.Model):
    activity_code = models.CharField(max_length = 255) # tXXXXXXXX
    descriptive_name = models.CharField(max_length = 255) 

    def __str__(self):
        return self.activity_code    

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
        
    household = models.ForeignKey(People) #TUCASEID 1
    statistical_weight = models.CharField(blank=True, max_length = 255) # TUFINLWGT 2
    children_present = models.IntegerField(blank=True, choices = YES_NO) # 1 yes, 2no TRYHHCHILD 3
    labor_force_status = models.IntegerField(blank=True, choices = LABOR_FORCE_STATUS) # 1 - 5 TELFS 10
    multiple_jobs = models.IntegerField(blank=True, choices = YES_NO) # 1 yes,2 no TEMJOT 11
    employment_type = models.IntegerField(blank=True, choices = EMPLOYMENT_TYPE) # 1F, 2P TRDPFTPT,12
    enrolled_in_school = models.IntegerField(blank=True, choices = YES_NO) # 1Y, 2N TESCHENR 13
    school_level = models.IntegerField(blank=True, choices = SCHOOL_LEVEL) #1 high school 2 college,TESCHLVL 14
    partner_present = models.IntegerField(blank=True, choices = PARTNER_PRESENT_TYPE) #1 spouse, 2Unmarried partner # None of these TRSPPRES 15
    partner_employed = models.IntegerField(blank=True, choices = YES_NO) # 1 emp, 2 not TESPEMPNOT, Is the partner employed? 16
    main_job_weekly_earning = models.IntegerField(blank=True, ) # In Cents TRERNWA, 17
    number_of_children = models.IntegerField(blank=True, ) # TRCHILDNUM children under 18 18
    partner_employment_status = models.IntegerField(blank=True, choices = EMPLOYMENT_TYPE)# 1 Ft, 2Pt, 3Varies, TRSPFTPT, 19
    work_week_hours = models.IntegerField(blank=True, ) # -4 hours vary TEHRUSLT, 20
    interview_day = models.IntegerField(blank=True, null=True, choices = WEEKDAYS) # 1-7, sunday-saturday TUDIARYDAY, 21
    interview_day_holiday = models.IntegerField(blank=True, choices = YES_NO) # 0 not, 1 yes TRHOLIDAY, 22
    time_for_eldercare = models.IntegerField(blank=True, ) # TRTEC, 23
    child_care_time = models.IntegerField(blank=True, ) # time to provide child Care TRTHH 24

    def __str__(self):
        return self.household.household_id.household_number
    
class Activity(models.Model):
    household_id = models.ForeignKey(Respondents) # TUCASEID
    activity = models.ForeignKey(ActivityList) # tXXXXXX
    time = models.IntegerField(blank=True ) # derived

    def __str__(self):
        return "{}: {} - {}".format(self.household_id, self.activity, self.time)
#not needed, included in class People
# class Sex(models.Model):
#     name = models.CharField(max_length = 10) # 1, 2 TESEX


