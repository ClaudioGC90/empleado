from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50) #nombre hace referencia como va aparecer este campo en el admin django
    shor_name = models.CharField('Nombre Corto', max_length=50, unique=True)
    anulate = models.BooleanField('Anulado', default=False)
    
    class meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Departamentos de la Empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name