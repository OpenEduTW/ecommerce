# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-03 17:18


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_add_ordermanager_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='journals_api_url',
        ),
    ]
