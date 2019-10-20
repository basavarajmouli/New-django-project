# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-17 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phonenumber', models.CharField(blank=True, max_length=100)),
                ('age', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Employee Info',
            },
        ),
    ]
