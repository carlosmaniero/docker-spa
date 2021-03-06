# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 03:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 25, 3, 40, 50, 309389, tzinfo=utc), verbose_name='Data de Criação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='indexed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Atualização'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='update_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 25, 3, 40, 53, 241403, tzinfo=utc), verbose_name='Data de Atualização'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 25, 3, 40, 55, 94389, tzinfo=utc), verbose_name='Data de Criação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.CharField(default='Outro', max_length=128, verbose_name='Motor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='indexed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Atualização'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='kms',
            field=models.PositiveIntegerField(default=0, verbose_name='Kilimetragem'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='update_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 25, 3, 41, 16, 81483, tzinfo=utc), verbose_name='Data de Atualização'),
            preserve_default=False,
        ),
    ]
