# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comments_comments_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
