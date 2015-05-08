# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20150320_1130'),
        ('characters', '0005_auto_20150320_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoDuel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agreed_a', models.NullBooleanField(default=False, verbose_name='Photographer A has agreed to duel')),
                ('agreed_b', models.NullBooleanField(default=False, verbose_name='Photographer B has agreed to duel')),
                ('winner', models.CharField(max_length=1, null=True, blank=True)),
                ('duel_start_time', models.DateTimeField(null=True, verbose_name='Duel start time', blank=True)),
                ('duel_end_time', models.DateTimeField(null=True, verbose_name='Duel end time', blank=True)),
                ('active', models.BooleanField(default=b'True', verbose_name='Is duel active')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('photo_a', models.ForeignKey(related_name='photo_a', verbose_name='Photo A', blank=True, to='photos.Photo', null=True)),
                ('photo_b', models.ForeignKey(related_name='photo_b', verbose_name='Photo B', blank=True, to='photos.Photo', null=True)),
                ('undecided', models.ManyToManyField(related_name='votes_undecided', null=True, to='characters.Photographer', blank=True)),
                ('votes_a', models.ManyToManyField(related_name='votes_a', null=True, to='characters.Photographer', blank=True)),
                ('votes_b', models.ManyToManyField(related_name='votes_b', null=True, to='characters.Photographer', blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Duel',
                'verbose_name_plural': 'Duels',
            },
            bases=(models.Model,),
        ),
    ]
