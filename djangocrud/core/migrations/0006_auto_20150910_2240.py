# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150611_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
    ]
