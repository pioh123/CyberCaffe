from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 30, verbose_name = "Nombres")
    last_name = models.CharField(max_length = 30, blank = True, null = True, verbose_name = "Apellidos")
    dni = models.IntegerField(unique=True)
    phone = models.CharField(max_length = 30, blank = True, null = True, verbose_name = "Telefono")
    money = models.FloatField(blank=True, null=True, verbose_name="Saldo (S/.)")
    register = models.DateTimeField(auto_now = True, auto_now_add=False)
    password = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50,unique=True,null=True, verbose_name="Email")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["first_name"]

    def __str__(self):
        return self.first_name

class Expend(models.Model):
    id = models.AutoField(primary_key= True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost = models.FloatField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales de gastos"