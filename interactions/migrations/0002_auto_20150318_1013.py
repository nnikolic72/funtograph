# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20150316_1036'),
        ('photos', '0003_auto_20150316_1312'),
        ('interactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('members_favoriters', models.ForeignKey(to='members.Member')),
                ('photo', models.ForeignKey(to='photos.Photo')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name': 'Favorite',
                'verbose_name_plural': 'Favorites',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='members_likers',
            new_name='members_commenters',
        ),
    ]
