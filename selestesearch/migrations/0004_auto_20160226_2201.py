# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selestesearch', '0003_auto_20160226_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seleste',
            old_name='review_text',
            new_name='featured_review_text',
        ),
        migrations.RenameField(
            model_name='seleste',
            old_name='review_title',
            new_name='featured_review_title',
        ),
    ]
