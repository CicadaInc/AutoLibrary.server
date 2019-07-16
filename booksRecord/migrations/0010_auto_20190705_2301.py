# Generated by Django 2.2.1 on 2019-07-05 18:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booksRecord', '0009_auto_20190629_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='takenbook',
            options={'get_latest_by': 'when_taken', 'ordering': ['is_returned', 'when_taken'], 'verbose_name': 'взятый экземпляр книги', 'verbose_name_plural': 'взятые экземпляры книг'},
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(db_index=True, help_text='Официальное наименование издательства, без слов "Издательство", "ООО", "ПАО" и т. п.', max_length=65, unique=True, verbose_name='наименование'),
        ),
        migrations.AlterField(
            model_name='takenbook',
            name='student',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='readersRecord.Student', verbose_name='ученик'),
        ),
        migrations.AlterField(
            model_name='takenbook',
            name='when_returned',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 18, 1, 11, 511113, tzinfo=utc), verbose_name='Дата и время возврата'),
        ),
        migrations.AddIndex(
            model_name='bookinstance',
            index=models.Index(fields=['status'], name='booksRecord_status_932cdd_idx'),
        ),
        migrations.AddIndex(
            model_name='takenbook',
            index=models.Index(fields=['is_returned'], name='booksRecord_is_retu_2f7bbb_idx'),
        ),
    ]