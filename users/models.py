from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_ready = models.BooleanField(default=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def days_left(self):
        today = datetime.date.today()
        remaining = (self.end_date - today).days
        return remaining

    def __str__(self):
        return f'{self.title}'
