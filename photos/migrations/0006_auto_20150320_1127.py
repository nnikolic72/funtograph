# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20150320_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_creation_date',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
