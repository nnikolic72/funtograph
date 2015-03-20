# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0006_auto_20150320_0914'),
        ('characters', '0004_photographer_max_photos_to_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoartlover',
            name='member',
        ),
        migrations.DeleteModel(
            name='PhotoArtLover',
        ),
        migrations.RemoveField(
            model_name='photojudge',
            name='member',
        ),
        migrations.DeleteModel(
            name='PhotoJudge',
        ),
        migrations.RemoveField(
            model_name='phototeammanager',
            name='member',
        ),
        migrations.DeleteModel(
            name='PhotoTeamManager',
        ),
        migrations.AlterModelOptions(
            name='photographer',
            options={'ordering': ('-level', '-current_xp', 'name'), 'get_latest_by': 'created_at'},
        ),
        migrations.RemoveField(
            model_name='photographer',
            name='character_type',
        ),
    ]
