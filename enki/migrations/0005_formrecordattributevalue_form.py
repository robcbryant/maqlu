# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enki', '0004_auto_20170217_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='formrecordattributevalue',
            name='form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enki.Form'),
            preserve_default=False,
        ),
    ]
