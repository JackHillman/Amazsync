# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160305_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttype',
            name='colour',
            field=models.CharField(choices=[('grey', 'Grey'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('red', 'Red'), ('pink', 'Pink'), ('purple', 'Purple')], default='grey', max_length=20),
        ),
    ]
