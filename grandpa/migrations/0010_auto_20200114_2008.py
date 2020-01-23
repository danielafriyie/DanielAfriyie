# Generated by Django 2.2.7 on 2020-01-14 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandpa', '0009_auto_20200112_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='about',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 20, 8, 33, 197416)),
        ),
        migrations.AlterField(
            model_name='myworkportfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 20, 8, 33, 272544)),
        ),
    ]