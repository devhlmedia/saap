# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('cerimonial', '0004_grupodecontatos'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupodecontatos',
            name='workspace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='grupodecontatos_set', to='core.AreaTrabalho', verbose_name='Área de Trabalho'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grupodecontatos',
            name='contatos',
            field=models.ManyToManyField(blank=True, related_name='grupodecontatos_set', to='cerimonial.Contato', verbose_name='Contatos do Grupo'),
        ),
    ]
