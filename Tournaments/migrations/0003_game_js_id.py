# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0002_auto_20141228_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='js_id',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
