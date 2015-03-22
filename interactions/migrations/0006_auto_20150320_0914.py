# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0005_like_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='members_commenters',
            field=models.ForeignKey(to='characters.Photographer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='members_favoriters',
            field=models.ForeignKey(to='characters.Photographer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like',
            name='members_likers',
            field=models.ForeignKey(to='characters.Photographer'),
            preserve_default=True,
        ),
    ]
