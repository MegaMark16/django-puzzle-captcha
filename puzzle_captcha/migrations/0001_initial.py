# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=b'', max_length=255, unique=True)),
                ('rows', models.IntegerField(default=0)),
                ('cols', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'originals')),
            ],
        ),
        migrations.CreateModel(
            name='PuzzlePiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'pieces')),
                ('order', models.IntegerField()),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle_captcha.Puzzle')),
            ],
        ),
    ]