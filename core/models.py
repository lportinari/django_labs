from django.db import models
from django.db.models.fields import DecimalField
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural: 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=20)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural: 'Montadoras'
    
    def __str__(self):
        return self.nome


def set_default_montadora():
    '''
    Se montadora "Padrão" não existir, criará um novo registro com nome "Padrão".
    '''
    return Montadora.objects.get_or_create(nome='Padrão')[0]  # (objeto, boolean)


class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return f'{self.montadora} {self.modelo}'
