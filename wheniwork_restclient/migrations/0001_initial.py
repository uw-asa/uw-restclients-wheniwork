# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('company', models.CharField(max_length=500)),
                ('master', models.ForeignKey(to='wheniwork_restclient.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('swap_id', models.PositiveIntegerField()),
                ('conversation_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('type', models.PositiveSmallIntegerField()),
                ('account', models.ForeignKey(to='wheniwork_restclient.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, b'Pending'), (1, b'Canceled'), (2, b'Accepted'), (3, b'Expired')])),
                ('type', models.PositiveSmallIntegerField(choices=[(0, b'Unpaid Time Off'), (1, b'Paid Time Off'), (2, b'Sick Leave'), (3, b'Holiday')])),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('hours', models.DecimalField(max_digits=5, decimal_places=2)),
                ('account', models.ForeignKey(to='wheniwork_restclient.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('notes', models.CharField(max_length=350)),
                ('account', models.ForeignKey(to='wheniwork_restclient.Account')),
                ('location', models.ForeignKey(to='wheniwork_restclient.Location')),
                ('position', models.ForeignKey(to='wheniwork_restclient.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
                ('location', models.ForeignKey(to='wheniwork_restclient.Location')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('employee_code', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='shift',
            name='site',
            field=models.ForeignKey(to='wheniwork_restclient.Site'),
        ),
        migrations.AddField(
            model_name='shift',
            name='user',
            field=models.ForeignKey(to='wheniwork_restclient.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='canceled_by',
            field=models.ForeignKey(related_name='+', to='wheniwork_restclient.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='creator',
            field=models.ForeignKey(related_name='+', to='wheniwork_restclient.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(to='wheniwork_restclient.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='request',
            field=models.ForeignKey(to='wheniwork_restclient.Request'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(to='wheniwork_restclient.User'),
        ),
    ]
