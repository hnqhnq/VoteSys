# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0021_auto_20180528_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='cTimes',
            field=models.IntegerField(default=0),
        ),
    ]
