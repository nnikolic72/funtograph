# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50, verbose_name='Photo attribute name')),
                ('description', models.CharField(default=b'', max_length=200, null=True, verbose_name='Photo attribute description', blank=True)),
                ('slug', models.SlugField(default=b'', blank=True, null=True, verbose_name='Photo attribute slug')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Photo Attribute',
                'verbose_name_plural': 'Photo Attributes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200, verbose_name='Photo category name')),
                ('description', models.CharField(default=b'', max_length=200, null=True, verbose_name='Photo category description', blank=True)),
                ('slug', models.SlugField(default=b'', blank=True, null=True, verbose_name='Photo category slug')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Photo Category',
                'verbose_name_plural': 'Photo Categories',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='author',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='photo',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Photo is active'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='attributes',
            field=models.ManyToManyField(to='photos.PhotoAttribute', null=True, verbose_name='Photo Attributes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='categories',
            field=models.ManyToManyField(to='photos.PhotoCategory', null=True, verbose_name='Photo Categories', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='for_sale',
            field=models.BooleanField(default=False, verbose_name='Photo is for sale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_wear',
            field=models.IntegerField(default=0, verbose_name='Photo wear'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='avg_photo_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, blank=True, null=True, verbose_name='Average photo rating'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Photo title'),
            preserve_default=True,
        ),
    ]
