from contextlib import nullcontext
from distutils.command.upload import upload
from typing import Match
from django.db import models
from django.conf import settings

# Create your models here.
class Caj(models.Model):
    name = models.CharField(max_length=200)
    components = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    price_with_shipping = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    stock = models.CharField(max_length=5)
    tea_image = models.ImageField(null=True, blank=True, upload_to='Images/')
    checked = models.BooleanField(default=False)


    def __str__(self):
        return self.name





