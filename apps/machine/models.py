from django.db import models
from apps.user.models import User

# Create your models here.

class Machine(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 50, null= True, blank= True)
    number = models.IntegerField()
    ip = models.CharField(max_length=15)
    start_time = models.DateTimeField(null= True, blank=True)
    end_time = models.DateTimeField(null= True, blank=True)
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null= True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maquina"
        verbose_name_plural = "Maquinas"


class Game(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 50)
    image = models.ImageField(upload_to='game',null= True, blank=True)
    url = models.CharField(max_length=100)

