# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserBase', '0008_user_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logged_in',
            field=models.BooleanField(default=True),
        ),
    ]