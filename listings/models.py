from django.db import models

# Create your models here.




class Kategorie(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name


class Objekt(models.Model):
    kategorie = models.ForeignKey(Kategorie,blank = True,null =True,related_name='mistnost',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name

class TypObjektu(models.Model):
    
    objekt = models.ForeignKey(Objekt,null=True, blank=True,related_name='objekt',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name
class Produkt(models.Model):

    pic = models.ImageField(upload_to='photos/%Kategorie/%Mistnost/%Objekt/%TypObjektu/')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    dostupnost = models.CharField(max_length=200)
    cena = models.IntegerField()
    typobjektu=models.ForeignKey(TypObjektu,blank = True,null =True,on_delete=models.PROTECT)
    objekt = models.ForeignKey(Objekt,blank = True,null =True,on_delete=models.PROTECT)
    def __str__(self):
        return self.name