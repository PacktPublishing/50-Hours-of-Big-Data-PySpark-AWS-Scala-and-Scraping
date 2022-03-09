from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
