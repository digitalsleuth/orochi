# Generated by Django 3.2 on 2020-08-02 14:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200730_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='parameter',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
