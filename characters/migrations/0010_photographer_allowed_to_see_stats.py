# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_photographer_allowed_to_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_see_stats',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
