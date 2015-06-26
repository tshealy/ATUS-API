# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respondents', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Relationship',
        ),
        migrations.DeleteModel(
            name='Sex',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.ForeignKey(to='respondents.ActivityList'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='household',
            field=models.ForeignKey(to='respondents.Respondents'),
        ),
        migrations.AlterField(
            model_name='people',
            name='household',
            field=models.ForeignKey(to='respondents.HouseholdList'),
        ),
    ]
