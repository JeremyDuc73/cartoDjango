from django.db import models


class savedPlace(models.Model):
    label = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
