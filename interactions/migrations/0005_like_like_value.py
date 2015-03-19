# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0004_comment_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like_value',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
