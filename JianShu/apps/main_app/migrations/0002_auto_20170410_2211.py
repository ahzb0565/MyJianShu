# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='auth',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]