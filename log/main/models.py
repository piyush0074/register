from django.db import models
from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published',default=timezone.localtime())

