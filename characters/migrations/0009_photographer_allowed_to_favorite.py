# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20150324_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_favorite',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
