# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'joining date'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name=b'last updated'),
        ),
    ]
