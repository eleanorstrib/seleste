# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('review_title', models.CharField(max_length=60)),
                ('review_text', models.TextField(max_length=1500)),
                ('overall_rating', models.CharField(max_length=1)),
                ('culture_values_rating', models.CharField(max_length=1)),
                ('management_rating', models.CharField(max_length=1)),
                ('compensation_benefits_rating', models.CharField(max_length=1)),
                ('opportunities_rating', models.CharField(max_length=1)),
                ('work_life_balance_rating', models.CharField(max_length=1)),
                ('recommend_to_friend_rating', models.CharField(max_length=1)),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
