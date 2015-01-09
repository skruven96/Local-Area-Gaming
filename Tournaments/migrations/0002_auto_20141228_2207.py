# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='teams',
            field=models.ManyToManyField(null=True, blank=True, to='Tournaments.Team'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
