# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indiancousin', '0002_menuitem_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='favorite',
            new_name='is_favorite',
        ),
    ]
