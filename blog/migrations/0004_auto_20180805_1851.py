# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-05 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180805_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='preview',
            field=models.URLField(blank=True, null=True),
        ),
    ]