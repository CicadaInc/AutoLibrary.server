# Generated by Django 2.2.1 on 2019-06-25 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booksRecord', '0003_auto_20190624_0807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='takenbook',
            old_name='date_time',
            new_name='when_taken',
        ),
        migrations.AddField(
            model_name='takenbook',
            name='when_returned',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 8, 42, 34, 425342, tzinfo=utc), verbose_name='Дата и время возврата'),
        ),
    ]