from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)