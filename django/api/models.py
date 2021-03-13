from django.db import models

# Create your models here.

class Produto(models.Model):
    
    name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=60)
    sold = models.PositiveIntegerField()