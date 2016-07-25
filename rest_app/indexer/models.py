from django.db import models


class IndexModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now=False,
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name='Data de Atualização',
        auto_now=True
    )
    indexed_at = models.DateTimeField(
        verbose_name='Data de Atualização',
        null=True, blank=True
    )

    class Meta:
        abstract = True
