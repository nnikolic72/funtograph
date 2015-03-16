# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_flickr_handle_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=cloudinary.models.CloudinaryField(max_length=100, null=True, verbose_name=b'image'),
            preserve_default=True,
        ),
    ]
