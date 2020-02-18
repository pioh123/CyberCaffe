from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='products',null= True, blank=True)
    stock = models.IntegerField(null= True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{0},{1}'.format(self.name,self.stock)

class Advertise(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='advertise',null= True, blank=True)
    description = models.TextField(blank=True,null=True)
    typea = models.IntegerField(blank=True, null=True)
   
class Promotion(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=20, blank=True, null=True,verbose_name="Promoción")
    image = models.ImageField(upload_to='promotion',null= True, blank=True)
