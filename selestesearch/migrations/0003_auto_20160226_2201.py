# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selestesearch', '0002_seleste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glassdoor',
            old_name='review_text',
            new_name='featured_review_text',
        ),
        migrations.RenameField(
            model_name='glassdoor',
            old_name='review_title',
            new_name='featured_review_title',
        ),
        migrations.RenameField(
            model_name='indeed',
            old_name='review_text',
            new_name='featured_review_text',
        ),
        migrations.RenameField(
            model_name='indeed',
            old_name='review_title',
            new_name='featured_review_title',
        ),
        migrations.AddField(
            model_name='company',
            name='number_ratings',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='glassdoor',
            name='number_ratings',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='indeed',
            name='number_ratings',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='seleste',
            name='number_ratings',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
