# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-18 15:16
from __future__ import unicode_literals

from django.db import migrations


def update_apc_status(apps, schema_editor):
    ArticleAPC = apps.get_model('apc', 'ArticleAPC')
    ArticleAPC.objects.filter(status='nopay').update(status='nonpay')


class Migration(migrations.Migration):
    dependencies = [
        ('apc', '0010_auto_20200618_1616'),
    ]

    operations = [
        migrations.RunPython(
            update_apc_status,
            reverse_code=migrations.RunPython.noop
        ),
    ]