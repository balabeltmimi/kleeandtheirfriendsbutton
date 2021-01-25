from django.db import models


class character(models.Model):

    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

