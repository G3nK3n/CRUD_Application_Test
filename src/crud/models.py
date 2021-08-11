from django.db import models

# Create your models here. CREATE IMAGEFIELD LATER
# makemigration + migrate everytime you make changes to the model
# Username = ken_s
class Motoneiges(models.Model):
    year = models.IntegerField()
    name = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

