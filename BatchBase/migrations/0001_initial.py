# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ShopperBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Earning', models.FloatField(blank=True, default=0.0)),
                ('ShopperId', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ShopperBase.Shopper')),
            ],
        ),
    ]