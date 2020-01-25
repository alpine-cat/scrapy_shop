from django.db import models


class Product(models.Model):
    p_url = models.CharField(max_length=256)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=256)
    price = models.CharField(max_length=16)
    images = models.TextField()
    sizes = models.CharField(max_length=100)
    description = models.TextField()
