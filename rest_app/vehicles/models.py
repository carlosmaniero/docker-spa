from django.db import models
from indexer.models import IndexModel


VEHICLE_COLORS = (
    ('azul', 'Azul'),
    ('preto', 'Preto'),
    ('prata', 'Prata'),
    ('vermelho', 'Vermelho'),
    ('verde', 'Verde'),
    ('outro', 'Outro')
)


VEHICLE_CATEGORY = (
    ('moto', 'Moto'),
    ('carro', 'carro')
)


class Manufacturer(IndexModel):
    name = models.CharField(
        verbose_name='Nome',
        max_length=64
    )


class Vehicle(IndexModel):
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        verbose_name='Fabricante'
    )
    model_name = models.CharField(
        verbose_name='Modelo',
        max_length=128
    )
    color = models.CharField(
        verbose_name='Cor',
        max_length=16,
        choices=VEHICLE_COLORS
    )
    category = models.CharField(
        verbose_name='Tipo',
        max_length=16,
        choices=VEHICLE_CATEGORY
    )
    kms = models.PositiveIntegerField(
        verbose_name='Kilimetragem',
        default=0
    )
    engine = models.CharField(
        verbose_name='Motor',
        max_length=128
    )
