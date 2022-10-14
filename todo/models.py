from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, default=None)
