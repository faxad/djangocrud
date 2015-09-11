# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('telephone', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name=b'joining date')),
                ('last_updated', models.DateTimeField(verbose_name=b'last updated')),
                ('remarks', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='supplier',
            field=models.OneToOneField(related_name='supplier', to='core.Supplier'),
        ),
    ]
