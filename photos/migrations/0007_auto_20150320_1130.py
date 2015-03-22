# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20150320_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='full_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
