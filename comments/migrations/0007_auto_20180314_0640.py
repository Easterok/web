# Generated by Django 2.0.2 on 2018-03-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20180313_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Ужасно'), (2, 'Плохо'), (3, 'Нормально'), (4, 'Хорошо'), (5, 'Отлично')], default=0),
        ),
    ]
