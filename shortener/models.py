from django.db import models

# Create your models here.
class ShortedURL(models.Model):
    full_url = models.CharField(max_length=500, unique=True)
    shorted = models.CharField(max_length=20, unique=True, db_index=True)
    counter = models.PositiveIntegerField(default=0)
