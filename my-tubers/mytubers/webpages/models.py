from django.db import models

# Create your models here.


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    button_link = models.URLField(
        max_length=255, null=True, default='https://www.google.co.in/')
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    fb_link = models.URLField(
        max_length=255, null=True, default='https://www.fb.com/')
    insta_link = models.URLField(
        max_length=255, null=True, default='https://www.instagram.com/')
    yt_link = models.URLField(
        max_length=255, default='https://www.youtube.com/')
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
