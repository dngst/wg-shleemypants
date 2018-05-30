# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-30 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='license_author',
            field=models.ForeignKey(blank=True, help_text='If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.', max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
