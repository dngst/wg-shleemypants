# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-15 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0005_auto_20180515_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealitem',
            name='meal_type',
            field=models.CharField(choices=[('actual meal', 'Actual meal'), ('planned meal', 'Planned meal')], default='planned meal', max_length=20),
        ),
    ]