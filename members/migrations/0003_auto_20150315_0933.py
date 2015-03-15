# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20150313_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('membership_start_time', models.DateTimeField(help_text='Date and time when the membership starts', verbose_name='Membership Start Time')),
                ('membership_end_time', models.DateTimeField(help_text='Date and time when the membership ends', verbose_name='Membership End Time')),
                ('active_membership', models.BooleanField(default=False, help_text='Checked if membership is active. Only one membership per member allowed', verbose_name='Is membership active')),
                ('suspended_membership', models.BooleanField(default=False, help_text='Checked if Membership is suspended', verbose_name='Suspended Membership')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('member', models.ForeignKey(blank=True, to='members.Member', help_text='Foreign key to Member object', null=True, verbose_name='Membership Owner')),
            ],
            options={
                'ordering': ['membership_end_time'],
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('membership_type_name', models.CharField(max_length=100)),
                ('membership_fee_type', models.CharField(max_length=10, choices=[(1, 'Free Membership'), (2, 'Paid Membership')])),
                ('membership_recurring_type', models.CharField(max_length=10, choices=[(1, 'Recurring Membership'), (2, 'Non-recurring Membership')])),
                ('active', models.BooleanField(default=True)),
                ('membership_fee_price', models.FloatField(default=0)),
                ('membership_duration', models.IntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['membership_type_name'],
                'verbose_name': 'MembershipType',
                'verbose_name_plural': 'MembershipTypes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_type',
            field=models.ForeignKey(blank=True, to='members.MembershipType', help_text='Membership type', null=True, verbose_name='Membership Type'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['user__username'], 'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
        migrations.AddField(
            model_name='member',
            name='beta_tester',
            field=models.BooleanField(default=False, help_text='Checked if Member is Beta tester', verbose_name='Beta tester'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='eyeem_handle',
            field=models.CharField(help_text='Your EyeEm account user name', max_length=30, null=True, verbose_name='EyeEm user name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='eyeem_handle_verified',
            field=models.BooleanField(default=False, help_text='Checked if mods verified members EyeEm handle', verbose_name='EyeEm handle verified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='facebook_url',
            field=models.CharField(help_text='Your Facebook profile URL', max_length=30, null=True, verbose_name='Facebook account URL', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='facebook_url_verified',
            field=models.BooleanField(default=False, help_text='Checked if mods verified members Facebook URL', verbose_name='Facebook URL verified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='flickr_handle',
            field=models.CharField(help_text='Your Flickr account user name', max_length=30, null=True, verbose_name='Flickr user name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='funtocredits',
            field=models.IntegerField(default=0, help_text='How much FuntoCredits Member has', verbose_name='FuntoCredits'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_handle',
            field=models.CharField(help_text='Your Instagram account user name', max_length=30, null=True, verbose_name='Instagram user name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_handle_verified',
            field=models.BooleanField(default=False, help_text='Checked if mods verified members Instagram handle', verbose_name='Instagram handle verified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='suspended',
            field=models.BooleanField(default=False, help_text='Checked if Member is suspended', verbose_name='Suspended'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='website',
            field=models.URLField(help_text='Your web site URL', null=True, verbose_name='Web Site URL', blank=True),
            preserve_default=True,
        ),
    ]
