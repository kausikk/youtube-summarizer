from django.db import models
import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Summarizer(models.Model):
    youtube_id = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    timestamp = ArrayField(JSONField())
    summary = ArrayField(models.TextField())
    time_summary_dict = JSONField()
