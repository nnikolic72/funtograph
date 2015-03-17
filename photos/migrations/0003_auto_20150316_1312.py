# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150316_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['title'], 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_price',
            field=models.IntegerField(default=0, verbose_name='Photo price'),
            preserve_default=True,
        ),
    ]
