# Generated by Django 2.2.1 on 2019-06-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readersRecord', '0002_auto_20190624_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[('1 классы', ((1, '1 «А»'), (2, '1 «Б»'), (3, '1 «В»'), (4, '1 «Г»'), (5, '1 «Д»'), (6, '1 «Е»'), (7, '1 «Ж»'))), ('2 классы', ((8, '2 «А»'), (9, '2 «Б»'), (10, '2 «В»'), (11, '2 «Г»'), (12, '2 «Д»'), (13, '2 «Е»'), (14, '2 «Ж»'))), ('3 классы', ((15, '3 «А»'), (16, '3 «Б»'), (17, '3 «В»'), (18, '3 «Г»'), (19, '3 «Д»'), (20, '3 «Е»'), (21, '3 «Ж»'))), ('4 классы', ((22, '4 «А»'), (23, '4 «Б»'), (24, '4 «В»'), (25, '4 «Г»'), (26, '4 «Д»'), (27, '4 «Е»'), (28, '4 «Ж»'))), ('5 классы', ((29, '5 «А»'), (30, '5 «Б»'), (31, '5 «В»'), (32, '5 «Г»'), (33, '5 «Д»'), (34, '5 «Е»'), (35, '5 «Ж»'))), ('6 классы', ((36, '6 «А»'), (37, '6 «Б»'), (38, '6 «В»'), (39, '6 «Г»'), (40, '6 «Д»'), (41, '6 «Е»'), (42, '6 «Ж»'))), ('7 классы', ((43, '7 «А»'), (44, '7 «Б»'), (45, '7 «В»'), (46, '7 «Г»'), (47, '7 «Д»'), (48, '7 «Е»'), (49, '7 «Ж»'))), ('8 классы', ((50, '8 «А»'), (51, '8 «Б»'), (52, '8 «В»'), (53, '8 «Г»'), (54, '8 «Д»'), (55, '8 «Е»'), (56, '8 «Ж»'))), ('9 классы', ((57, '9 «А»'), (58, '9 «Б»'), (59, '9 «В»'), (60, '9 «Г»'), (61, '9 «Д»'), (62, '9 «Е»'), (63, '9 «Ж»'))), ('10 классы', ((64, '10 «А»'), (65, '10 «Б»'), (66, '10 «В»'), (67, '10 «Г»'), (68, '10 «Д»'), (69, '10 «Е»'), (70, '10 «Ж»'))), ('11 классы', ((71, '11 «А»'), (72, '11 «Б»'), (73, '11 «В»'), (74, '11 «Г»'), (75, '11 «Д»'), (76, '11 «Е»'), (77, '11 «Ж»')))], help_text='номер и литера класса', verbose_name='класс'),
        ),
    ]