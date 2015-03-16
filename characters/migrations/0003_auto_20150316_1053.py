# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20150315_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoartlover',
            name='character_type',
            field=models.CharField(default='Photo Art Lover', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photographer',
            name='character_type',
            field=models.CharField(default='Photographer', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photojudge',
            name='character_type',
            field=models.CharField(default='Photo Judge', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phototeammanager',
            name='character_type',
            field=models.CharField(default='Photo Team Manager', max_length=50),
            preserve_default=True,
        ),
    ]
