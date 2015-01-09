# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seats', '0002_auto_20141231_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='unique_str_id',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
