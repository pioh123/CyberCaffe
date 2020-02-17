from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(User):
    dni = models.IntegerField(unique=True)
    phone = models.CharField(max_length = 30, blank = True, null = True )
    money = models.FloatField(blank=True, null=True)
    hoard = models.FloatField(blank=True, null=True)
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    def __str__(self):
        return self.username



class Expend(models.Model):
    id = models.AutoField(primary_key= True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost = models.FloatField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales de gastos"


class Promotion(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=20, blank=True, null=True,verbose_name="Promoción")
