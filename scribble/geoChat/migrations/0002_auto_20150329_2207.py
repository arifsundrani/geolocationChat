# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geoChat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='poster',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 3, 30, 2, 7, 23, 642000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='spam',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
