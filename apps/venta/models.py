from django.db import models
from apps.cliente.models import Cliente
<<<<<<< HEAD
from apps.Productos.models import Productos
from apps.bases.models import ClassModelo
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b

# Create your models here.
from django.db import models


class Venta(models.Model):
    cliente=models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    fecha_ventas=models.DateTimeField(auto_now_add=True)
    valor=models.IntegerField()
<<<<<<< HEAD
    cantidad=models.CharField(max_length=1000)
=======
    cantidad=models.CharField( max_length=1000)
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)
