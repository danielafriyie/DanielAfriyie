# Generated by Django 2.2.7 on 2020-01-12 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandpa', '0005_auto_20200107_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=255)),
                ('linkedin', models.CharField(blank=True, max_length=255)),
                ('github', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 12, 21, 44, 26, 157982))),
            ],
        ),
        migrations.CreateModel(
            name='MyWorkPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=255)),
                ('work_details', models.TextField()),
                ('work_link', models.CharField(blank=True, max_length=255)),
                ('work_image', models.ImageField(upload_to='Work/Image/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 12, 21, 44, 26, 227495))),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='WorkPortfolio',
        ),
    ]
