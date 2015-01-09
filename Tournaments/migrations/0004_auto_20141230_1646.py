# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0003_game_js_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='lost',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='won',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
