# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoArtLover',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('current_xp', models.IntegerField(default=0)),
                ('total_xp', models.IntegerField(default=0)),
                ('character_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'get_latest_by': 'created_at',
                'verbose_name': 'Photo Art Lover',
                'verbose_name_plural': 'Photo Art Lovers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('current_xp', models.IntegerField(default=0)),
                ('total_xp', models.IntegerField(default=0)),
                ('character_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'get_latest_by': 'created_at',
                'verbose_name': 'Photographer',
                'verbose_name_plural': 'Photographers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoJudge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('current_xp', models.IntegerField(default=0)),
                ('total_xp', models.IntegerField(default=0)),
                ('character_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'get_latest_by': 'created_at',
                'verbose_name': 'Photo Judge',
                'verbose_name_plural': 'Photo Judges',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoTeamManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('current_xp', models.IntegerField(default=0)),
                ('total_xp', models.IntegerField(default=0)),
                ('character_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'get_latest_by': 'created_at',
                'verbose_name': 'Photo Team Manager',
                'verbose_name_plural': 'Photo Team Managers',
            },
            bases=(models.Model,),
        ),
    ]
