# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PwdManager', '0002_auto_20170925_1350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account111',
            new_name='Account',
        ),
    ]
