# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreBase', '0009_auto_20170709_1955'),
        ('Products', '0004_auto_20170709_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='StoreId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='StoreBase.Store'),
        ),
    ]