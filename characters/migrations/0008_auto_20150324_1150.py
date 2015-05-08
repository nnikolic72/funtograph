# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20150324_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_comment',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photographer',
            name='allowed_to_like',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
