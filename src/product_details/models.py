from django.db import models

# Create your models here.
class Details(models.Model):
    year = models.IntegerField()
    name = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_number = models.IntegerField()