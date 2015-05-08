# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20150316_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='current_energy',
            field=models.IntegerField(default=0, help_text='How much Energy Member has', verbose_name='Current Energy'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='max_energy',
            field=models.IntegerField(default=0, help_text='How much Energy Member can have', verbose_name='Max Energy'),
            preserve_default=True,
        ),
    ]
