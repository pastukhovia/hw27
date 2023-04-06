from django.db import models


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=True)
    author = models.CharField(max_length=1000, null=True)
    price = models.FloatField(null=True)
    desc = models.CharField(max_length=1000, null=True)
    address = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=True)
