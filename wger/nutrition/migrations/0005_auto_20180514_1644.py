# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-14 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Language', verbose_name='Language'),
        ),
    ]