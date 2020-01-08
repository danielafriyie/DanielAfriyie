# Generated by Django 2.2.7 on 2020-01-07 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 7, 19, 0, 34, 445597))),
            ],
        ),
        migrations.CreateModel(
            name='WorkPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=255)),
                ('work_details', models.TextField()),
                ('work_link', models.CharField(max_length=255)),
                ('work_image', models.ImageField(upload_to='Work/Image/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 7, 19, 0, 34, 501858))),
            ],
        ),
    ]