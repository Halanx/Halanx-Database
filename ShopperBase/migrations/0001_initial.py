# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('PhoneNo', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=1000, null=True)),
                ('EmailId', models.EmailField(blank=True, max_length=254)),
                ('City', models.CharField(blank=True, default=b'Delhi', max_length=200, null=True)),
                ('IdNumber', models.CharField(blank=True, max_length=50)),
                ('IdType', models.CharField(choices=[(b'Aadhar Card', b'Aadhar Card'), (b'Voter Id Card', b'Voter Id Card')], default=b'Aadhar Card', max_length=100)),
                ('Vehicle', models.CharField(blank=True, choices=[(b'Car', b'Car')], default=b'Car', max_length=50)),
                ('AvgRating', models.FloatField(blank=True, default=3.0, null=True)),
                ('n', models.IntegerField(blank=True, default=0)),
                ('Verified', models.BooleanField(default=False)),
                ('AvailableDate', models.DateField(blank=True, null=True)),
                ('AvailableFrom', models.TimeField(blank=True, null=True)),
                ('AvailableTo', models.TimeField(blank=True, null=True)),
                ('A', models.IntegerField(blank=True, default=0)),
                ('B', models.IntegerField(blank=True, default=0)),
                ('C', models.IntegerField(blank=True, default=0)),
                ('D', models.IntegerField(blank=True, default=0)),
                ('E', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
