from django.db import models
from datetime import datetime


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.full_name
