# Generated by Django 2.2.7 on 2020-01-07 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandpa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 19, 4, 33, 546726)),
        ),
        migrations.AlterField(
            model_name='workportfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 19, 4, 33, 622680)),
        ),
    ]