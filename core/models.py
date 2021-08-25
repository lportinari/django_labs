from django.db import models
from django.db.models.fields import DecimalField

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural: 'Chassis'

    def __str__(self):
        return self.numero


class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, models.CASCADE)
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return self.modelo
