# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoChat', '0002_auto_20150329_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroom',
            old_name='name',
            new_name='room_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='chat_room',
            field=models.ForeignKey(blank=True, to='geoChat.ChatRoom', null=True),
            preserve_default=True,
        ),
    ]
