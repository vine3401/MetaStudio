# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_app_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
