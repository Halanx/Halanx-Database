# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsList', '0003_auto_20170618_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='Item',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
