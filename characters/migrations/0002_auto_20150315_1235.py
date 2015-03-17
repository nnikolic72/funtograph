# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150315_0933'),
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoartlover',
            name='member',
            field=models.ForeignKey(to='members.Member', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photographer',
            name='member',
            field=models.ForeignKey(to='members.Member', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photojudge',
            name='member',
            field=models.ForeignKey(to='members.Member', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phototeammanager',
            name='member',
            field=models.ForeignKey(to='members.Member', null=True),
            preserve_default=True,
        ),
    ]
