# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PwdManager', '0003_auto_20170925_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
