# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160305_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('yeo_tag', models.CharField(default=models.CharField(max_length=30), max_length=100)),
            ],
        ),
    ]