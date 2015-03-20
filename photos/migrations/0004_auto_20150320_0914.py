# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20150316_1036'),
        ('photos', '0003_auto_20150316_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phototophotographer',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='phototophotographer',
            name='photographer',
        ),
        migrations.DeleteModel(
            name='PhotoToPhotographer',
        ),
        migrations.AddField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(blank=True, to='members.Member', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ManyToManyField(to='characters.Photographer', null=True, blank=True),
            preserve_default=True,
        ),
    ]
