# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20150316_1036'),
        ('photos', '0003_auto_20150316_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=300, null=True, blank=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('members_likers', models.ForeignKey(to='members.Member')),
                ('photo', models.ForeignKey(to='photos.Photo')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('members_likers', models.ForeignKey(to='members.Member')),
                ('photo', models.ForeignKey(to='photos.Photo')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
            bases=(models.Model,),
        ),
    ]
