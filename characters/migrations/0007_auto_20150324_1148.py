# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_photographer_last_vote_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_duel',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_found_collective',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_join_league',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_team_duel',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
