# Generated by Django 2.2.1 on 2019-06-14 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksRecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='takenbook',
            options={'verbose_name': 'взятый экземпляр книги', 'verbose_name_plural': 'взятые экземпляры книг'},
        ),
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booksRecord.Subject', verbose_name='предмет'),
        ),
    ]