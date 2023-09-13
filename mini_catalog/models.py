from django.db import models


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    image = models.FileField(upload_to='images/')
    stats = models.JSONField()
    price = models.IntegerField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
