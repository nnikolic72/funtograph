# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0002_auto_20150318_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(help_text='Comment up to 300 characters. Be polite!', max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='members_commenters',
            field=models.ForeignKey(to='characters.PhotoArtLover'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='members_favoriters',
            field=models.ForeignKey(to='characters.PhotoArtLover'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like',
            name='members_likers',
            field=models.ForeignKey(to='characters.PhotoArtLover'),
            preserve_default=True,
        ),
    ]
