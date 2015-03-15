# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150315_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='flickr_handle_verified',
            field=models.BooleanField(default=False, help_text='Checked if mods verified members Flickr handle', verbose_name='Flickr handle verified'),
            preserve_default=True,
        ),
    ]
