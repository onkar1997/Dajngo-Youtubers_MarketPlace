# Generated by Django 4.1.4 on 2022-12-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=100)),
                ('button_link', models.URLField(default='https://www.google.co.in/', max_length=255, null=True)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=100)),
                ('fb_link', models.URLField(default='https://www.fb.com/', max_length=255, null=True)),
                ('insta_link', models.URLField(default='https://www.instagram.com/', max_length=255, null=True)),
                ('yt_link', models.URLField(default='https://www.youtube.com/', max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]