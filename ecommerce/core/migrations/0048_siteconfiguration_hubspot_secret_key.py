# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-20 16:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_businessclient_enterprise_customer_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='hubspot_secret_key',
            field=models.CharField(blank=True, help_text='Secret key for Hubspot portal authentication', max_length=255, verbose_name='Hubspot Portal Secret Key'),
        ),
    ]
