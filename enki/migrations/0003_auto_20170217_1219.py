# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enki', '0002_auto_20170217_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormRecordAttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(max_length=50)),
                ('form_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enki.FormType')),
            ],
        ),
        migrations.CreateModel(
            name='FormRecordAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_value', models.CharField(max_length=50)),
                ('form_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enki.FormRecordAttributeType')),
            ],
        ),
        migrations.RemoveField(
            model_name='formrecordattribute',
            name='form_type',
        ),
        migrations.RemoveField(
            model_name='form',
            name='form_record_attribute',
        ),
        migrations.DeleteModel(
            name='FormRecordAttribute',
        ),
        migrations.AddField(
            model_name='form',
            name='form_record_attribute_type',
            field=models.ManyToManyField(to='enki.FormRecordAttributeType'),
        ),
    ]
