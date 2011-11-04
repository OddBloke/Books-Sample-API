from django.db import models


class Shelf(models.Model):

    location = models.CharField(max_length=255)


class Book(models.Model):

    title = models.CharField(max_length=255)
    shelf = models.ForeignKey(Shelf, related_name='books')
