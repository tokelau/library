# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_book_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='section',
            field=models.TextField(default='other'),
        ),
    ]
