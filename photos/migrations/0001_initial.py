# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('photo', cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'image')),
                ('avg_photo_rating', models.DecimalField(default=0, null=True, max_digits=3, decimal_places=2, blank=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['user__username'],
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoToPhotographer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_author', models.BooleanField(default=True)),
                ('is_manager', models.BooleanField(default=False)),
                ('photo', models.ForeignKey(to='photos.Photo')),
                ('photographer', models.ForeignKey(to='characters.Photographer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='author',
            field=models.ManyToManyField(to='characters.Photographer', through='photos.PhotoToPhotographer'),
            preserve_default=True,
        ),
    ]
