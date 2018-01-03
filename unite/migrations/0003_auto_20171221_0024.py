# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unite', '0002_auto_20171221_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_resources', to='unite.Resource'),
        ),
        migrations.AlterUniqueTogether(
            name='applicationresource',
            unique_together=set([('resource', 'app_id')]),
        ),
    ]
