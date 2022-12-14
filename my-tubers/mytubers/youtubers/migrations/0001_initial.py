# Generated by Django 4.1.4 on 2022-12-07 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/youtuber/%Y/%m/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('crew', models.CharField(max_length=255)),
                ('camera_type', models.CharField(max_length=255)),
                ('subscriber_count', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
