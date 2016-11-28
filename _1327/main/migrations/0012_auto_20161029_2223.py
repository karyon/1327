# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-29 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_add_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='documents.Document', verbose_name='Document'),
        ),
    ]