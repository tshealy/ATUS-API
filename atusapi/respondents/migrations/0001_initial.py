# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityList',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('activity_code', models.CharField(max_length=255)),
                ('descriptive_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdList',
            fields=[
                ('household_number', models.CharField(serialize=False, primary_key=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('respondent_identifier', models.CharField(blank=True, max_length=2)),
                ('age', models.IntegerField(default=1, blank=True)),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], blank=True)),
                ('relationship_to_respondent', models.IntegerField(choices=[(18, 'Self'), (19, 'Self'), (20, 'Spouse'), (21, 'Unmarried Partner'), (22, 'Own household child'), (23, 'Grandchild'), (24, 'Parent'), (25, 'Brother/sister'), (26, 'Other relative'), (27, 'Foster child'), (28, 'Housemate/roommate'), (29, 'Roomer/boarder'), (30, 'Other non relative'), (40, 'Own non household child under 18')], blank=True)),
                ('household_id', models.ForeignKey(to='respondents.HouseholdList')),
            ],
        ),
        migrations.CreateModel(
            name='Respondents',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('statistical_weight', models.CharField(blank=True, max_length=255)),
                ('children_present', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')], blank=True)),
                ('labor_force_status', models.IntegerField(choices=[(1, 'Employed - at Work'), (2, 'Employed - Absent'), (3, 'Unemployed - On Layoff'), (4, 'Unemployed - Looking'), (5, 'Not in labor force')], blank=True)),
                ('multiple_jobs', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')], blank=True)),
                ('employment_type', models.IntegerField(choices=[(1, 'Full Time'), (2, 'Part Time'), (3, 'Varies')], blank=True)),
                ('enrolled_in_school', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')], blank=True)),
                ('school_level', models.IntegerField(choices=[(1, 'High School'), (2, 'College/University')], blank=True)),
                ('partner_present', models.IntegerField(choices=[(1, 'Spouse Present'), (2, 'Unmarried Partner Present'), (3, 'No Spouse or Unmarried Partner')], blank=True)),
                ('partner_employed', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')], blank=True)),
                ('main_job_weekly_earning', models.IntegerField(blank=True)),
                ('number_of_children', models.IntegerField(blank=True)),
                ('partner_employment_status', models.IntegerField(choices=[(1, 'Full Time'), (2, 'Part Time'), (3, 'Varies')], blank=True)),
                ('work_week_hours', models.IntegerField(blank=True)),
                ('interview_day', models.IntegerField(choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')], null=True, blank=True)),
                ('interview_day_holiday', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')], blank=True)),
                ('time_for_eldercare', models.IntegerField(blank=True)),
                ('child_care_time', models.IntegerField(blank=True)),
                ('household', models.ForeignKey(to='respondents.People')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activity',
            field=models.ForeignKey(to='respondents.ActivityList'),
        ),
        migrations.AddField(
            model_name='activity',
            name='household_id',
            field=models.ForeignKey(to='respondents.Respondents'),
        ),
    ]
