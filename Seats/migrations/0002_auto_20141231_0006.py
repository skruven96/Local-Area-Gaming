# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='owned_by',
            field=models.ForeignKey(to='Seats.Ticket', null=True, blank=True),
            preserve_default=True,
        ),
    ]
