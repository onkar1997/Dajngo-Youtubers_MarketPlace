from django.db import models
from datetime import datetime

class HireYoutuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField(max_length=255, blank=True)
    user_id = models.IntegerField(blank=True)
    youtuber_id = models.IntegerField()
    youtuber_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
