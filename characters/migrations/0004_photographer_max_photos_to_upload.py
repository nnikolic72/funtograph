# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20150316_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='max_photos_to_upload',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
