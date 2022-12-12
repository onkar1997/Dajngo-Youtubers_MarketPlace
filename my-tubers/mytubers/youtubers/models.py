from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Youtuber(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    crew_choices = (
        ('Solo', 'Solo'),
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    camera_choices = (
        ('Canon', 'Canon'),
        ('Sony', 'Sony'),
        ('Nikon', 'Nikon'),
        ('Panasonic', 'Panasonic'),
        ('Olympus', 'Olympus'),
        ('Pentax', 'Pentax'),
        ('other', 'other'),
    )

    category_choices = (
        ('Vlogs', 'Vlogs'),
        ('Film-making', 'Film-making'),
        ('Cooking', 'Cooking'),
        ('Comedy', 'Comedy'),
        ('Educational', 'Educational'),
        ('Spiritual', 'Spiritual'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=255)
    gender = models.CharField(choices=gender_choices, max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtuber/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    subscriber_count = models.IntegerField()
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
