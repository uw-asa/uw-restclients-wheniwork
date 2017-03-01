# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheniwork_restclient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='position',
            field=models.ForeignKey(to='wheniwork_restclient.Position', null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='site',
            field=models.ForeignKey(to='wheniwork_restclient.Site', null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='location',
            field=models.ForeignKey(to='wheniwork_restclient.Location', null=True),
        ),
    ]
