# Generated by Django 2.2.1 on 2019-06-29 13:10

import booksRecord.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booksRecord', '0008_auto_20190629_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.PositiveIntegerField(help_text='идентификатор книги, уникальный для каждого экземпляра; совпадает с номером штрихкода на наклейке', primary_key=True, serialize=False, unique=True, validators=[booksRecord.validators.ean8_validator], verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='takenbook',
            name='book_instance',
            field=models.ForeignKey(editable=False, limit_choices_to={'status': 0}, on_delete=django.db.models.deletion.CASCADE, to='booksRecord.BookInstance', verbose_name='экземпляр книги'),
        ),
        migrations.AlterField(
            model_name='takenbook',
            name='when_returned',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 19, 13, 10, 8, 192824, tzinfo=utc), verbose_name='Дата и время возврата'),
        ),
    ]