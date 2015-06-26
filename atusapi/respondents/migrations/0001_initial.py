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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ActivityList',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('activity_code', models.CharField(max_length=255)),
                ('descriptive_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdList',
            fields=[
                ('household_number', models.CharField(primary_key=True, max_length=255, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('respondent_identifier', models.CharField(max_length=2)),
                ('age', models.IntegerField(default=1)),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('relationship_to_respondent', models.IntegerField(choices=[(18, 'Self'), (19, 'Self'), (20, 'Spouse'), (21, 'Unmarried Partner'), (22, 'Own household child'), (23, 'Grandchild'), (24, 'Parent'), (25, 'Brother/sister'), (26, 'Other relative'), (27, 'Foster child'), (28, 'Housemate/roommate'), (29, 'Roomer/boarder'), (30, 'Other non relative'), (40, 'Own non household child under 18')])),
                ('household', models.ForeignKey(to='respondents.HouseholdList')),
            ],
        ),
        migrations.CreateModel(
            name='Respondents',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('statistical_weight', models.CharField(max_length=255)),
                ('children_present', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')])),
                ('multiple_jobs', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')])),
                ('employment_type', models.IntegerField(choices=[(1, 'Full Time'), (2, 'Part Time'), (3, 'Varies')])),
                ('school_level', models.IntegerField(choices=[(1, 'High School'), (2, 'College/University')])),
                ('partner_present', models.IntegerField(choices=[(1, 'Spouse Present'), (2, 'Unmarried Partner Present'), (3, 'No Spouse or Unmarried Partner')])),
                ('partner_employed', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')])),
                ('main_job_weekly_earning', models.IntegerField()),
                ('number_of_children', models.IntegerField()),
                ('partner_employment_status', models.IntegerField(choices=[(1, 'Full Time'), (2, 'Part Time'), (3, 'Varies')])),
                ('work_week_hours', models.IntegerField()),
                ('inteview_day', models.IntegerField(choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')])),
                ('interview_day_holiday', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')])),
                ('time_for_eldercare', models.IntegerField()),
                ('child_care_time', models.IntegerField()),
                ('enrolled_in_school', models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (0, 'No - 0')])),
                ('labor_force_status', models.IntegerField(choices=[(1, 'Employed - at Work'), (2, 'Employed - Absent'), (3, 'Unemployed - On Layoff'), (4, 'Unemployed - Looking'), (5, 'Not in labor force')])),
                ('household', models.ForeignKey(to='respondents.HouseholdList')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activity',
            field=models.ForeignKey(to='respondents.ActivityList'),
        ),
        migrations.AddField(
            model_name='activity',
            name='household',
            field=models.ForeignKey(to='respondents.Respondents'),
        ),
    ]
