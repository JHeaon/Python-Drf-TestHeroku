from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    bid = models.IntegerField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateTimeField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
