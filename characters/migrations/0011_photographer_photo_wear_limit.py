# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_photographer_allowed_to_see_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='photo_wear_limit',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
