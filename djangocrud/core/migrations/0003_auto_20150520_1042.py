# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150502_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='contact_person',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='supplier',
            field=models.ForeignKey(to='core.Supplier'),
        ),
    ]
