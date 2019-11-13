# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-18 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20190718_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('books', models.ManyToManyField(related_name='author_name', to='books_authors_app.Book')),
            ],
        ),
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
        migrations.DeleteModel(
            name='Authors',
        ),
    ]
