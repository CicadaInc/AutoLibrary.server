# Generated by Django 2.2.1 on 2020-08-21 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksRecord', '0012_auto_20200820_1201'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TakenBook',
        ),
    ]