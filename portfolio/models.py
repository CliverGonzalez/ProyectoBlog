from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
