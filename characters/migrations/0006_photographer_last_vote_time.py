# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20150320_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='last_vote_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
