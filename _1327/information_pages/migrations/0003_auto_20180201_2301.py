# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-01 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information_pages', '0002_informationdocument_is_menu_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informationdocument',
            options={'base_manager_name': 'objects', 'permissions': (('view_informationdocument', 'User/Group is allowed to view that document'),), 'verbose_name': 'Information document', 'verbose_name_plural': 'Information documents'},
        ),
    ]
