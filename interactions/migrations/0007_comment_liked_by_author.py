# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0006_auto_20150320_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked_by_author',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
