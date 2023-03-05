from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    author = models.TextField()
    date = models.DateField()
    read_duration = models.TextField()
    content = models.TextField()
    label = models.TextField()
