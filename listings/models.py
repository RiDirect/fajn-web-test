from django.db import models

# Create your models here.
class Produkt(models.Model):
    pic = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.CharField(max_length=200)
    dostupnost = models.CharField(max_length=200)
    cena = models.IntegerField()
    