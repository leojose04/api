from django.contrib import admin
from .models import programmer, Stu

# Register your models here.

admin.site.register(programmer)# se registra el modelos para poder verlo en el panel de administracion
admin.site.register(Stu)