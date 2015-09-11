# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150601_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='supplier',
            field=models.ForeignKey(related_name='contactinfo', to='core.Supplier'),
        ),
    ]
