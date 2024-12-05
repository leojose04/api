from django.db import models

# Create your models here.
#Aqui se crean los modelos (las tablas "relacionales" o colecciones "no relaciones")
class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10,null=True, default=None)
    is_active = models.BooleanField(default=True) 

class Stu(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    Numero_ficha = models.CharField(max_length=7)
    Formacion  = models.BooleanField(default=True)
    Fecha = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)
