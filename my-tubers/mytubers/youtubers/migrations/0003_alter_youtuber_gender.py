# Generated by Django 4.1.4 on 2022-12-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_alter_youtuber_camera_type_alter_youtuber_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255),
        ),
    ]