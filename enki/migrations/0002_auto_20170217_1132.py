# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formrecordattribute',
            old_name='form_parent',
            new_name='form_type',
        ),
    ]
