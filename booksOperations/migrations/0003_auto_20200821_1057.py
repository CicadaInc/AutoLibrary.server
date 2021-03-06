# Generated by Django 2.2.1 on 2020-08-21 05:57

import booksOperations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksOperations', '0002_auto_20200821_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktaking',
            name='when_returned',
            field=models.DateTimeField(blank=True, default=booksOperations.models.BookTaking.get_return_date, null=True, verbose_name='Дата и время возврата'),
        ),
    ]
