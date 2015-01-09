# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('str_id', models.CharField(max_length=3, default='Z00')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('payed', models.BooleanField(default=False)),
                ('unique_str_id', models.CharField(max_length=40)),
                ('owned_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(to='Seats.Seat', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seat',
            name='owned_by',
            field=models.ForeignKey(to='Seats.Ticket'),
            preserve_default=True,
        ),
    ]
