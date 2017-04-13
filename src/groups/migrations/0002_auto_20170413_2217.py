# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='support_groups', through='groups.Membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supportgroup',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='events', to='groups.SupportGroupTag'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membership',
            name='support_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='groups.SupportGroup'),
        ),
    ]
