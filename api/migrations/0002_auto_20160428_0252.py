# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
